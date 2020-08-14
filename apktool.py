#!/usr/local/bin/python3.8

import os,sys
from adbx.adbx import *
from adbx.apkx import *

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Yazhou.Xie's command tool")
    parser.add_argument("-d", "--detail", dest="detail", action="store_true", help="Display apk manifest detail")
    parser.add_argument("-u", "--uninstall", dest="uninstall", action="store_true", help="uninstall apk")
    parser.add_argument("-i","--install", dest="install", action="store_true", help="Install apk")
    parser.add_argument("-ui", "--un-install", dest="uninstall_install", action="store_true", help="uninstall and install apk")
    parser.add_argument("-s", "--start", dest="start", action="store_true", help="start LaunchableActivity")
    parser.add_argument("-sw","--start-w", dest="start_W", action="store_true", help="start -W LaunchableActivity")
    parser.add_argument("-sd","--start-D", dest="start_D", action="store_true", help="start -D LaunchableActivity")
    parser.add_argument("-uis", "--un-ins-start", dest="uninstall_install_start", action="store_true", help="uninstall and install apk and start LaunchableActivity")
    parser.add_argument("-uisw", "--un-ins-startW", dest="uninstall_install_start_W", action="store_true", help="uninstall and install apk and start -W LaunchableActivity")
    parser.add_argument("-p", "--pm-clear", dest="pm_clear", action="store_true", help="pm clear apk")
    parser.add_argument("-ps", "--pmclear-start", dest="pm_clear_start", action="store_true", help="pm clear apk and start LaunchableActivity")
    parser.add_argument("-psw", "--pmclear-start-W", dest="pm_clear_start_W", action="store_true", help="pm clear apk and start -W LaunchableActivity")
    parser.add_argument("-ks", "--kill-sign", dest="kill_sign", action="store_true", help="kill sign check for apk")
    parser.add_argument("-si", "--sign", dest="sign", action="store_true", help="sign apk to {dirname}/ori.signed.apk")
    
    parser.add_argument("apk", action="store", help="The apk file path")

    args = parser.parse_args()
    
    apkpath = os.path.abspath(args.apk)
    manifest = AndroidManifest(apkpath)
    adbx = adbx(apkpath, manifest=manifest)
    apkx = apkx(apkpath, manifest=manifest)
    if args.detail:
        adbx.print_apk()
    if args.uninstall:
        adbx.uninstall()
    if args.install:
        adbx.install()
    if args.uninstall_install:
        adbx.uninstall()
        adbx.install()
    if args.start:
        adbx.start(time=False, num=1)
    if args.start_W:
        adbx.start(time=True, num=1)
    if args.start_D:
        adbx.start(time=False, num=1)
    if args.uninstall_install_start:
        adbx.uninstall()
        adbx.install()
        adbx.start(time=False, num=1)
    if args.uninstall_install_start_W:
        adbx.uninstall()
        adbx.install()
        adbx.start(time=True, num=1)
    if args.pm_clear:
        adbx.pmclear()
    if args.pm_clear_start:
        adbx.pmclear()
        adbx.start(time=False)
    if args.pm_clear_start_W:
        adbx.pmclear()
        adbx.start(time=True)
    if args.sign:
        adbx.apksign()
    
    if args.kill_sign:
        apkx.kill_signcheck()