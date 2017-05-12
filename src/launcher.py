#
#   FOX LAUNCHER
#   
#   Created for Fur Desktop Environment
#   http://github.com/krushndayshmookh/fur-box
#     
#   Created by Krushn Dayshmookh
#   http://krushndayshmookh.github.io
#
#




import sys
# import subprocess
from os import system
from os import listdir


files = listdir("/usr/share/applications")
files.sort()

#print (files)


appList = []

class AnApp:
    """An app information object"""
    name = "n"
    executable = "e"
    icon = "e"

def readAppName (desktopFile):
    x = AnApp()
    file = open (desktopFile,"r")
    lines = file.readlines()
    for data in lines:
        prop = data.split("=")

        if prop[0] == "Name":
            prop[1] = prop[1].replace("\n","")
            prop[1] = prop[1].replace(" ","-")
            x.name = prop[1]
          
        if prop[0] == "TryExec":
            prop[1] = prop[1].replace("\n","")
            x.executable = prop[1]
           
        if prop[0] == "Icon":
            prop[1] = prop[1].replace("\n","")
            x.icon = prop[1]
            #print (appIcon + "\n")
        #app = AnApp(appName, appExec, appIcon)
        
        #
    #print (x.name)
    appList.append(x)
    #print (appList[0].name,appList[0].executable,appList[0].icon,)        
    file.close()


for filename in files:    
    readAppName("/usr/share/applications"+"/"+filename)
#readAppName("deluge.desktop")


def list():  
    for app in appList:
        print (app.name)

    
#print (appList)    
    
def runProgram(program):
    for app in appList:
        if app.name == program:
            print app.name
            system(app.executable)
  
if sys.argv[1] == "run":
    runProgram(sys.argv[2])
    
if sys.argv[1] == "list":
    list()
    
#print sys.argv[0]
#print sys.argv[1]
#print sys.argv[2]
    
    
# -------------------------------------------------------------------------------------------------
#
#       USAGE INSTRUCTIONS
#
#   use "python launcher.py list"  to list all applications in /usr/share/applications
#
#
#   after that to run "app-name" from the list use "python launcher.py run app-name"
#     
#
#   This is currently very much in development.
#   It may not work at all some times.
#
#  
#
#
#
#     
#
#
#
#  

