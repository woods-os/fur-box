# Fur Box
> An Elegant, Lightweight Desktop Environment

### About
This is an `openbox` based desktop environment which has very few dependencies. Designed to be beautiful, lightning fast and stable.

![screenshot1](https://github.com/krushndayshmookh/fur-box/raw/master/docs/images/screenshot-current.png)

### Install instructions

**This is currently very much in developmental stage. Lots of work is to be done. Themes and configurations may not work as expected. Still, it is more stable than other desktops such as GNOME and KDE.**

#### Arch Linux:
* the `base-devel` package needs to be installed. if not already, install it with:  
`$ sudo pacman -S base-devel git wget`  

* install [obmenu-generator from AUR](https://aur.archlinux.org/packages/obmenu-generator/)  
`$ git clone https://aur.archlinux.org/obmenu-generator.git`  
`$ cd obmenu-generator`  
`$ makepkg -sri`  

* download `arch-install.sh`:  
`$ wget https://github.com/krushndayshmookh/fur-box/releases/download/v0.1-alpha1/arch-install.sh`

* make it executable:  
`$ chmod a+x arch-install.sh`

* run it:  
`$ ./arch-install.sh`  
Say Yes to prompts and enter password wherever reqiured.

* Log out and log back into your newly installed Fur Box Desktop!

* if you want icon theme, you can install it:  
`$ git clone https://aur.archlinux.org/papirus-icon-theme-git.git`  
`$ cd papirus-icon-theme-git`  
`$ makepkg -sri` 

* also, the GTK+ theme:  
`$ sudo pacman -S arc-gtk-theme`  

### Basic Components
* `openbox` as window manager  
* `nitrogen` for desktop background  
* `compton` as compositor  
* `tint2` for panel  
* `obmenu-generator` to generate dynamic menus  
* `plank` as dock  

### Themes
* `arc-gtk-theme` as GTK+ theme  
* `fur-box` for window decorations  
* `papirus-icon-theme` for icons  
* `paper-cursor-theme` for cursors  

### Recommended Apps
  _Will be added soon._  
  _Will be included in another package as well._
  

### Developed by
#### [Krushn Dayshmookh](http://krushndayshmookh.github.io)

