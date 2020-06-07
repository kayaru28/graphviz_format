filename=$1
. ./ftp_param

ftp -n <<END
open ${IP}
user ${USER} ${PASS}
binary
put ${filename}
END
