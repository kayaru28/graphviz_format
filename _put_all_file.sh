#!/bin/sh
for filename in `ls -1`
do
  echo ${filename}
  sh _ftp.sh ${filename}
done

