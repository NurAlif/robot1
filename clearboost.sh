#!/bin/bash
sudo apt-get -y --purge remove libboost-all-dev libboost-doc libboost-dev
echo "clear boost dir"
sudo rm -r /usr/local/lib/libboost*
sudo rm -r /usr/local/include/boost
sudo rm -f /usr/lib/libboost_*
sudo rm -r /usr/include/boost
