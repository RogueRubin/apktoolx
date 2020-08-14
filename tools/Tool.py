#!/usr/bin/python3.8

import os,sys
from tools.Log import LOG
import subprocess

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def exec_command(cmd, log=False, allow_fail=False, status=False, allow_waring=True):
    if log :
        LOG.info("Begin exec %s"%cmd)

    try:
        a,b = subprocess.getstatusoutput(cmd)
        if a != 0 :
            if not allow_fail:
                print("exec fail :\n%s%s%s\n%s"%(bcolors.FAIL, cmd, bcolors.ENDC, b))
                exit()
            elif allow_waring:
                print("Waring : \n%s%s%s\n%s"%(bcolors.FAIL, cmd, bcolors.ENDC, b))
        elif a == 0:
            print("%sexec %s success%s"%(bcolors.OKGREEN, cmd, bcolors.ENDC))
    except Exception as e:
        if not allow_fail:
            print("exec fail :\n%s%s%s"%(bcolors.FAIL, cmd, bcolors.ENDC))
            raise Exception("exec failed")
        elif allow_waring:
            print("Waring : \n%s%s%s\n"%(bcolors.FAIL, cmd, bcolors.ENDC))
    
    
    if status:
        return a,b
    else:
        return b

def output(function):
    def func(*args, **kwargs):
        print("----------------- %12s -----------------"%function.__name__)
        b = function(*args, **kwargs)
        print("%s\n"%(str(b)))
        return b
    return func

CURR_DIR = os.path.dirname(__file__)

PLATFORM = "macos" if sys.platform.index("darwin") >=0 else "linux" if sys.platform.index("linux") >=0 else "windows" 

AAPT = "%s/%s/aapt/30.0.0/aapt2"%(CURR_DIR, PLATFORM)
ADB = "%s/%s/adb/30.0.0/adb"%(CURR_DIR, PLATFORM)

JKS = "%s/public/debug.jks"%(CURR_DIR)
APK_SIGNER = "%s/%s/apksigner/29.0.0/apksigner"%(CURR_DIR, PLATFORM)

SMALI = "java -jar %s/public/smali-2.4.0.jar "%(CURR_DIR)
BAKSMALI = "java -jar %s/public/baksmali-2.4.0.jar "%(CURR_DIR)

MY_SMALI_DIR="%s/public/smali"%(CURR_DIR)
NoSignApplicationdex = "%s/public/NoSignApplication.dex"%(CURR_DIR)

AXML="java -jar %s/public/axml-1.0.jar"%(CURR_DIR)

FIX_SMALI="java -jar %s/public/fixmethod-all-1.8.jar"%(CURR_DIR)