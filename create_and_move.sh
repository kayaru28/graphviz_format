#!/bin/sh
cd /graphviz

for filename in `ls -1 *.dot`
do
filename=`basename $filename .dot`
dot -Tgif ${filename}.dot -o ${filename}.gif
done

ftp -n <<END
open 10.0.0.1
user anonymous anonymous
binary
put *.gif
END



