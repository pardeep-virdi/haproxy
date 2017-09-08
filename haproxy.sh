#!/bin/bash

echo "this HA-proxy will listen on localhost 80 port"


echo "Please provide backend server info"

echo "web server1 IP"

read web01ip

echo "web server1 port"

read web01port

echo "web server2 IP"

read web02ip

echo "web server2 port"

read web02port



python sample.py web01ip web01port web02ip web02port





