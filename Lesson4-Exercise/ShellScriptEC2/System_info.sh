#!/bin/bash

echo "---system Info---"
echo "You are using $(cat /etc/issue)"
echo "Your Kernel version is $(uname -r)"
echo "Your virtual memory is $(free -h)"