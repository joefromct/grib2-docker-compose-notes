#!/bin/bash

#export DEBIAN_FRONTEND=noninteractive
echo "System Update.."
apt -y update &&
apt -y upgrade &&
echo "package installs..." &&
conda install -y -c anaconda xarray pandas &&
conda install -y -c conda-forge pynio &&
echo "Done"
