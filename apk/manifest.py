#!/usr/local/bin/python3.8
# -*- coding: UTF-8 -*-

from tools.Tool import *
from tools.Log import *

import os,sys

class AndroidManifest(object):
    """Parse AndroidManifest.xml ."""

    def __init__(self, apk_file=None):
        super(AndroidManifest, self).__init__()
        self.apk_file = apk_file
        if is_zip(self.apk_file) and self.is_have_manifest(): 
            self.parse_manifest()
    
    def is_have_manifest(self):
        manifest = exec_command("zipinfo %s | grep \"AndroidManifest.xml\" | wc -l"%(self.apk_file), doing=False)
        return int(manifest) > 0
    
    def parse_manifest(self):
        b = exec_command("%s dump badging %s AndroidManifest.xml"%(AAPT, self.apk_file), log=False, allow_fail=True, allow_waring=False, doing=False)
        if not b:
            raise Exception("Parse %s of AndroidManifest.xml Error !"%self.apk_file)
        self.pkgname = None
        self.minSdkVerision = None
        self.targetSdkVerision = None
        self.appLabel = None
        self.launchableActivity = None
        self.applicaionName = None
        self.debuggable = None
        self.appComponentFactory = None
        for line in b.split('\n'):
            if line.startswith('package:'):
                self.parse_package(line)
            if line.startswith('sdkVersion:'):
                self.parse_minSdk(line)
            if line.startswith('targetSdkVersion:'):
                self.parse_targetSdk(line)
            if line.startswith('application-label:'):
                self.parse_app_label(line)
            if line.startswith('launchable-activity:'):
                self.parse_launchable_activity(line)
        
        self.parse_application()

    # parse package line
    def parse_package(self, pkg_line):
        key_values = pkg_line[len('package: '):].split(' ')
        for key_value in key_values:
            if key_value.startswith('name='):
                self.pkgname = self.strip_attr( key_value[len('name='):] )
            if key_value.startswith('versionCode='):
                self.versionCode = self.strip_attr( key_value[len('versionCode='):] )
            if key_value.startswith('versionName='):
                self.versionName = self.strip_attr( key_value[len('versionName='):] )

    def parse_minSdk(self, line):
        self.minSdkVerision = self.strip_attr( line[len('sdkVersion:'):] )
    
    def parse_targetSdk(self, line):
        self.targetSdkVerision = self.strip_attr( line[len('targetSdkVersion:'):] )
    
    def parse_app_label(self, line):
        self.appLabel = self.strip_attr( line[len('application-label:'):] )

    def parse_launchable_activity(self, line):
        key_values = line[len('launchable-activity:'):].split(' ')
        for key_value in key_values:
            if key_value.startswith('name='):
                self.launchableActivity = self.strip_attr( key_value[len('name='):] ) 

    def strip_attr(self, _attr):
        if not _attr:
            return _attr
        _attr = _attr.strip()
        if _attr.startswith('\''):
            _attr = _attr[1:]
        if _attr.endswith('\''):
            _attr = _attr[:-1]
        
        if _attr.startswith('"'):
            _attr = _attr[1:]
        if _attr.endswith('"'):
            _attr = _attr[:-1]
        return _attr

    def parse_application(self):
        exec_command("unzip %s AndroidManifest.xml -d %s/.manifestcache"%(self.apk_file, CURR_DIR), allow_fail=False, doing=False)
        try:
            b = exec_command("%s read %s/.manifestcache/AndroidManifest.xml application"%(AXML, CURR_DIR), allow_fail=True, doing=False)
            for line in b.splitlines():
                if line:
                    key_values = line.split(':')
                    if len(key_values) == 2:
                        if key_values[0] == "name":
                            self.applicaionName = key_values[1]
                        if key_values[0] == "debuggable":
                            self.debuggable = True if key_values[1] == "true" else False
                        if key_values[0] == "appComponentFactory":
                            self.appComponentFactory = key_values[1]
        except expression as identifier:
            pass
        finally:
            os.remove("%s/.manifestcache/AndroidManifest.xml"%(CURR_DIR))
            os.removedirs("%s/.manifestcache/"%(CURR_DIR))

    def toString(self):
        return "package\t\t: %s\n" \
        "minSdk\t\t: %s\n" \
        "targSdk\t\t: %s\n" \
        "label\t\t: %s\n" \
        "launch\t\t: %s\n" \
        "applicaion\t: %s\n" \
        "debug\t\t: %s\n" \
        "appComponentFac\t: %s\n" \
        %(self.pkgname, self.minSdkVerision, self.targetSdkVerision, self.appLabel, self.launchableActivity, self.applicaionName, self.debuggable, self.appComponentFactory)
