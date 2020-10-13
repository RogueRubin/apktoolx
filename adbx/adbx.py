#!/usr/bin/python3.8

import os,sys
from apk.manifest import *
from tools.Tool import *

class adbx(object):
    def __init__(self, inApk, manifest, sdevice=""):
        self.inApk = inApk
        self.device = sdevice
        self.adb = ADB
        if self.device:
            self.adb = "%s -s %s"%(ADB, self.device)
        self.manifest = manifest
    
    def print_apk(self):
        print(self.manifest.toString())
    
    @output
    def install(self):
        return exec_command("%s install %s"%(self.adb, self.inApk))

    @output
    def uninstall(self, allow_fail = True):
        b = exec_command("%s uninstall %s"%(self.adb, self.manifest.pkgname), allow_fail=allow_fail, status=False)
        if "Unknown package" in b :
            return "Unknow package : %s"%(self.manifest.pkgname)
        return b

    @output
    def start(self, time = False, debug=False, num = 1):
        W = ""
        if time:
            W = "-W"
        D = ""
        if debug:
            D = "-D -n "
        return exec_command("%s shell am start %s %s %s/%s"%(self.adb, W, D, self.manifest.pkgname, self.manifest.launchableActivity))
    
    @output
    def pmclear(self):
        return exec_command("%s shell pm clear '%s'"%(self.adb, self.manifest.pkgname))

    @output
    def apksign(self, jks=JKS):
        return exec_command("%s sign --ks %s --ks-key-alias debugkey --ks-pass pass:qwe123 --key-pass pass:qwe123 --out %s.signed.apk %s"%(APK_SIGNER, jks, self.inApk[0:-4], self.inApk))

if __name__ == "__main__":
    pass