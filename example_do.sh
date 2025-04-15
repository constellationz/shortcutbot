#!/usr/bin/env bash

case $1 in
    start)
        sudo systemctl start minecraft.service
        ;;
    stop)
        sudo systemctl stop minecraft.service
        ;;
    restart)
        sudo systemctl restart minecraft.service
        ;;
    uname)
        uname -a
        ;;
    *)
        echo "start, stop, restart, uname"
    esac
