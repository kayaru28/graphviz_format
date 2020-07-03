#!/bin/sh
filename=$1

sh _ftp_pull.sh ${filename}.dot
dot -Tgif ${filename}.dot -o ${filename}.gif
sh _ftp.sh ${filename}.gif
