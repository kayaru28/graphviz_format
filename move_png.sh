#!/bin/sh
cd /root

for filename in `ls -1 | grep .png`
do
  echo ${filename}
  sh ftp.sh ${filename}
done

