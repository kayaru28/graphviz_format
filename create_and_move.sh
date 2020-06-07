#!/bin/sh
cd /root

for filename in `ls -1 *.dot`
do
  filename=`basename $filename .dot`
  echo *****get${filename}
  dot -Tgif ${filename}.dot -o ${filename}.gif
done

for filename in `ls -1`
do
  sh ftp.sh ${filename}
done

