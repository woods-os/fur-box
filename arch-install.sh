#!/bin/bash

# install dependencies:
sudo pacman -S openbox tint2 plank nitrogen compton
#obmenu-generator to be added soon with other aur packages.

# clone or download this repository:
git clone http://github.com/krushndayshmookh/fur-box.git

# move into folder:
cd furbox

# copy the folders:
cp -rf user-home/.config $HOME
sudo cp -rf usr /
sudo cp -rf etc /

# set permissions
# user files
sudo chmod 755 ~/.config/openbox/autostart
sudo chmod 755 ~/.config/openbox/environment
sudo chmod 755 ~/.config/openbox/menu.xml
sudo chmod 755 ~/.config/openbox/power-menu.xml
sudo chmod 755 ~/.config/openbox/rc.xml

sudo chmod 755 ~/.config/obmenu-generator/schema.pl

sudo chmod 755 ~/.config/nitrogen/bg-saved.cfg

sudo chmod 755 ~/.config/tint2/tint2rc

# system files
sudo chmod 755 /usr/local/bin/fur-box-session
sudo chmod 755 /usr/share/xsessions/fur-box.desktop

sudo chmod 755 /usr/share/backgrounds/Godafoss_Iceland.jpg

sudo chmod 755 /usr/share/plank/themes/*/dock.theme


# reconfigure oenbox
openbox --reconfigure

