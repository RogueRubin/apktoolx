#!/bin/bash

while getopts "su" arg ; do
    case $arg in
        s)
            SET=true
            ;;
    	u)
	    UNSET=true
            ;;
        ?)  
            echo "usage: -s setproxy -u unset proxy"
            exit 1
        ;;
    esac
done

if [ ${SET+x} ];then
    git config --global http.proxy '[http://127.0.0.1:1087](http://127.0.0.1:1087/)'
    echo "http.proxy:127.0.0.1:1087"
    git config --global https.proxy '[https://127.0.0.1:1087](https://127.0.0.1:1087/)'
    echo "https.proxy:127.0.0.1:1087"
elif [ ${UNSET+x} ];then
    git config --global --unset http.proxy
    echo "unset http.proxy"
    git config --global --unset https.proxy
    echo "unset https.proxy"
fi
