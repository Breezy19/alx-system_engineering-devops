#!/usr/bin/env bash
# This script writes "I am alive!" to the file /tmp/my_process with a 2-second pause between messages.

while true; do
    echo "I am alive!" >> /tmp/my_process
    sleep 2
done
