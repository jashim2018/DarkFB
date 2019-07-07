#!/data/data/com.termux/files/usr/bin/bash

if [ $(dpkg-query -W -f='${Status}' coreutils 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
  pkg install coreutils -y;
fi
git pull origin master
