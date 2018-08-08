#!/bin/sh

sudo apt-get update && sudo apt-get upgrade
sudo apt-get install python -y
sudo apt-get install python-pip -y

pip install numpy scipy
pip install -U scikit-learn
pip install googlemaps
pip install pandas


#install tools to see plots in windows usin X11 server

sudo apt-get update && sudo apt-get install x11-apps -y
sudo apt-get install gnome-calculator -y         #LOL, this get all the gnone GTK stuff
sudo apt-get install qtbase5-dev -y
apt-get install python-tk -y
pip install matplotlib

echo "export DISPLAY=localhost:0.0" | tee -a ~/.bashrc

echo "---------------------------------------------------------"
echo "Download and RUN https://sourceforge.net/projects/xming/"
echo "---------------------------------------------------------"
