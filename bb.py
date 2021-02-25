#!/usr/local/bin/python3.8

from tools.bb.b_tool import *
from tools.Tool import *

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Yazhou.Xie's BB command tool")

    parser.add_argument("-c", "--config", dest="config", action="store_true", help="Display apk manifest detail")

    parser.add_argument("apk", action="store", help="The apk file path")

    args = parser.parse_args()

    if args.config:
        b = exec_command("%s %s"%(PACKEE_CONFIG, args.apk))
        print(b)