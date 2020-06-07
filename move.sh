#!/bin/sh
cd /root/dist/

for filename in `ls -1`
do
  echo ${filename}
  sh ftp.sh ${filename}
done

