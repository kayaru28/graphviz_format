#!/bin/sh
sh ftp_pull.sh create_and_move.sh
sh ftp_pull.sh ftp.sh
sh ftp_pull.sh ftp_pull.sh
sh ftp_pull.sh move.sh
sh ftp_pull.sh move_png.sh
sh ftp_pull.sh move_special.sh
sh ftp_pull.sh refresh.sh




