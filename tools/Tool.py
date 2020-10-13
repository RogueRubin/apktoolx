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

def exec_command(cmd, log=False, allow_fail=False, status=False, allow_waring=True, doing=True):
    if log :
        LOG.info("Begin exec %s"%cmd)

    try:
        a,b = subprocess.getstatusoutput(cmd)
        if a != 0 :
            if not allow_fail:
                print("exec fail :\n%s%s%s\n%s"%(bcolors.FAIL, cmd, bcolors.ENDC, b))
                exit()
            elif allow_waring:
                print("Waring : \n%s%s%s\n"%(bcolors.FAIL, cmd, bcolors.ENDC))
        elif a == 0 and doing:
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
        print("%s%s%s\n"%(bcolors.OKBLUE, str(b), bcolors.ENDC))
        return b
    return func

def is_zip(zip_file):
    a,b = exec_command("zipinfo %s"%(zip_file), status=True, allow_fail=True, allow_waring=False, doing=False)
    return a == 0

def is_dex(dex_file):
    with open(dex_file,"rb") as _dex:
        try:
            buf = _dex.read(6)
            left_num = 0
            for i in range(0,6):
                #print("i : %d"%(i))
                left_num = ( buf[i] << 8 * (5-i) ) | left_num
            #print("left_num : %d == 110386968408115"%left_num)
            return left_num == 110386968408115
        except Exception as identifier:
            raise identifier
        finally:
            _dex.close()

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