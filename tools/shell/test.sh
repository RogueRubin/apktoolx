
cur_dir=$(pwd)
old_apk="com.duxiaoman.umoney.protect.signed0805.apk"
new_apk="com.duxiaoman.umoney.protect.signed0814.apk"
pkg_name="com.duxiaoman.umoney"
tmp="/data/local/tmp"

if [ ! -d ${cur_dir}/screen ];then
    mkdir ${cur_dir}/screen
else 
    echo ${cur_dir}/screen exist
fi

echo "adb push ${cur_dir}/app/${old_apk} ${tmp}"
adb push ${cur_dir}/app/${old_apk} ${tmp}

echo "adb push ${cur_dir}/app/${new_apk} ${tmp}"
adb push ${cur_dir}/app/${new_apk} ${tmp}

for (( i = 0; i < 500; i++ )); do
    echo  $i;

    adb uninstall ${pkg_name}
    echo "1.卸载app"

    echo "2.安装老app, adb shell pm install /sdcard/${old_apk}"
    adb shell pm install ${tmp}/${old_apk}

    adb logcat -c 

    echo "3.启动app"
    adb shell am start -n com.duxiaoman.umoney/com.duxiaoman.umoney.home.SplashActivity

    echo "4.延时3s"
    sleep 3

    adb shell "screencap -p /sdcard/screenshot${i}0.png"
    
    echo "5.关闭app"
    adb shell am force-stop ${pkg_name}

    echo "6.覆盖安装新app, adb shell pm install  -r /sdcard/${new_apk}"
    adb shell pm install  -r ${tmp}/${new_apk}

    echo "7.启动app"
    adb shell am start -n com.duxiaoman.umoney/com.duxiaoman.umoney.home.SplashActivity

    echo "8.延时3s"
    sleep 3

    echo "9.截图和日志"
    adb shell "screencap -p /sdcard/screenshot${i}1.png"
    adb pull /sdcard/screenshot${i}0.png ${cur_dir}/screen/screenshot${i}0.png
    adb pull /sdcard/screenshot${i}1.png ${cur_dir}/screen/screenshot${i}1.png
    adb logcat -d -v threadtime > ${cur_dir}/screen/log${i}.txt

    sleep 1

done;
