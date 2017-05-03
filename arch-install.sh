#!/bin/bash

# install dependencies:
sudo pacman -S openbox tint2 plank nitrogen compton
#obmenu-generator to be added soon with other aur packages.

# clone or download this repository:
git clone http://github.com/krushndayshmookh/fur-box.git

#move into folder:
cd furbox

# copy the folders:
cp -rf user-home/.config $HOME
sudo cp -rf usr /
sudo cp -rf etc /
