#!/bin/bash
sudo -i
hostnamectl set-hostname ("hostname")
apt update -y && apt upgrade -y
apt install -y docker.io
cat<<EOF>>/etc/hosts
(internal ip) swarm1
(internal ip) swarm2
(internal ip) swarm3
(internal ip) storage
(internal ip) agent
EOF

docker swarm join --token ("TOKEN") swarm1:2377