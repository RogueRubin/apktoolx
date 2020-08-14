#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-

import os,sys
from apk.manifest import *
from tools.Tool import *
import base64

class apkx(object):
    def __init__(self, inApk, manifest):
        self.inApk = inApk
        self.workspace = "%s/workspace"%(os.path.abspath('.'))
        if os.path.exists(self.workspace):
            os.removedirs(self.workspace)
        os.makedirs(self.workspace)
        self.manifest=manifest
        self.mac_mach = "''" if PLATFORM=="macos" else ""

    def get_superclass(self, smali_path):
        with open(smali_path) as smail_file:
            for line in smail_file.readlines():
                if line.startswith(".super"):
                    return line.lstrip(".super").strip()
        
        return None

    # clazz = "Lcom/example/demo;"
    def find_class_path(self, clazz, dexdir):
        dexes = [os.path.join(dexdir, name) for name in os.listdir(dexdir) if name.endswith('.dex')]
        for dexitem in dexes:
            b = exec_command("%s list classes %s"%(BAKSMALI, dexitem))
            print(clazz)
            if b.find(clazz) >=0 :
                exec_command("%s d %s -o %s"%(BAKSMALI, dexitem, dexitem[0:-4]), allow_fail=False)
                smali_path = "%s/%s"%(dexitem[0:-4], clazz[1:-1])
                super_class = self.get_superclass("%s.smali"%smali_path)
                if super_class == 'Landroid/app/Application;':
                    return smali_path,dexitem
                else:
                    exec_command("rm -rf %s"%(dexitem[0:-4]))
                    return self.find_class_path(super_class, dexdir)
                
        return None,None

    def splitKey(self, s,start,head,tail):
        i = s.find(head,start)
        if i != -1 :
            i = i + len(head)
            j = s.find(tail,i)
            return (j,s[i:j])
        else:
            return (start,'')

    def parse_cert(self, rsa_file):
        content = exec_command("openssl pkcs7 -inform DER -in '%s' -print_certs -text" % rsa_file, allow_fail=False)
        i,cert_base64 = self.splitKey(content,0,'-----BEGIN CERTIFICATE-----','-----END CERTIFICATE-----')
        cert = cert_base64.replace('\n','')
        return cert

    @output
    def kill_signcheck(self):
        try:
            outapk = "%s.killsign.apk"%(self.inApk[0:-4])
            exec_command("cp -f %s %s"%(self.inApk, outapk), log = True, status=True)
            '''
            # Plan 1
            exec_command("unzip %s classes.dex -d %s"%(self.inApk, self.workspace), log = True, status=True)
            exec_command("%s d %s/classes.dex -o %s/classes"%(BAKSMALI, self.workspace, self.workspace), log = True, status=True)
            exec_command("cp -rf %s/xyz %s/classes"%(MY_SMALI_DIR, self.workspace), log = True, status=True)
            exec_command("%s a %s/classes -o %s/classes.dex"%(SMALI, self.workspace, self.workspace), log = True, status=True)
            exec_command("cd %s && zip -rD %s classes.dex && cd -"%(self.workspace, outapk), log = True, status=True)
            '''
            # Plan 2
            dexdir = "%s/dex"%self.workspace
            exec_command("unzip %s classes*.dex -d %s"%(self.inApk, dexdir),allow_fail=False)
            # 查找 application 并且进行修改
            if self.manifest.applicaionName:
                applicaionSmali = "L%s;"%(self.manifest.applicaionName.replace('.','/').strip())
                smali_path,dexitem = self.find_class_path(applicaionSmali, dexdir)
                if not smali_path:
                    print("Can't find application smali")
                    exit()
                exec_command("sed -i %s 's#.super Landroid/app/Application;#.super Lxyz/NoSignApplication;#g' %s.smali"%(self.mac_mach, smali_path))
                exec_command("sed -i %s 's#Landroid/app/Application;->#Lxyz/NoSignApplication;->#g' %s.smali"%(self.mac_mach, smali_path))
                exec_command("%s a %s -o %s && rm -rf %s"%(SMALI, dexitem[0:-4], dexitem, dexitem[0:-4]))
            
            # 拆分classes.dex
            filter_list = ['Landroid/support','Landroidx']
            if self.manifest.applicaionName:
                filter_list.append('L%s'%(self.manifest.applicaionName.replace('.','/').strip()))
            filter_list_str = ','.join([ item for item in filter_list])
            dex_num = exec_command("zipinfo %s \"classes*.dex\" | wc -l"%(self.inApk), allow_fail=False)
            dest_dex = "classes%d.dex"%(int(dex_num)+1)
            exec_command("%s split-dex --input-dex \"%s/classes.dex\" --out-dex \"%s/%s\" --filter \"%s\""%(FIX_SMALI, dexdir, dexdir, dest_dex, filter_list_str), allow_fail=False)
            # 合并dex
            splitdir = "%s/split"%(dexdir)
            exec_command("unzip %s META-INF/*.RSA META-INF/*.DSA -d %s"%(outapk, self.workspace), allow_fail=True)
            for _file in os.listdir("%s/META-INF"%self.workspace):
                if _file.endswith(".RSA") or _file.endswith(".DSA"):
                    cert = self.parse_cert("%s/META-INF/%s"%(self.workspace,_file))
                    exec_command("mkdir %s/smali && cp -rf %s/xyz %s/smali"%(self.workspace, MY_SMALI_DIR, self.workspace), allow_fail=False)
                    exec_command("find %s/smali -name NoSignApplication.smali | xargs sed -i %s 's@### Signatures Data ###@%s@g'"%(self.workspace, self.mac_mach,cert))
                    exec_command("%s a %s/smali -o %s/NoSignApplication.dex"%(SMALI, self.workspace, self.workspace), allow_fail=False)
                    exec_command("rm -rf %s/smali"%(self.workspace))
                    break
            exec_command("mkdir -p %s && mv %s/classes.dex %s"%(splitdir, dexdir, splitdir), allow_fail=False)
            exec_command("mv %s/NoSignApplication.dex %s/classes2.dex"%(self.workspace, splitdir), allow_fail=False)
            exec_command("%s Megedex -i %s -o %s"%(FIX_SMALI, splitdir, dexdir), allow_fail=False)
            exec_command("rm -rf %s"%(splitdir), allow_fail=False)
            exec_command("cd %s && zip -rD %s classes*.dex && cd -"%(dexdir, outapk), allow_fail=False)
            #修改Manifest
            exec_command("unzip %s AndroidManifest.xml -d %s && mv %s/AndroidManifest.xml %s/old.xml"%(outapk, self.workspace, self.workspace, self.workspace), allow_fail=False)
            exec_command("%s modify %s/old.xml %s/app.xml %s && rm -f %s/old.xml"%(AXML, self.workspace, self.workspace, self.manifest.applicaionName, self.workspace), allow_fail=False)
            exec_command("%s modify %s/app.xml %s/AndroidManifest.xml debugable && rm -f %s/app.xml"%(AXML, self.workspace, self.workspace, self.workspace), allow_fail=False)
            exec_command("cd %s && zip -rD %s AndroidManifest.xml && rm -f AndroidManifest.xml && cd -"%(self.workspace, outapk),allow_fail=False)
            return "kill sign check success:\n%s"%outapk
        except Exception as e:
            return "kill sign check failed"
        finally:
            exec_command("rm -rf %s"%self.workspace)