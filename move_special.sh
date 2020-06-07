#!/bin/sh
cd /root

for filename in `ls -1 | grep $1`
do
  echo ${filename}
  sh ftp.sh ${filename}
done

