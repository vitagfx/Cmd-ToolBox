# Script by Vitag : https://link.gallery.vitag

import os, sys

os.system('@echo off')
os.system('title Cmd-ToolBox - Vitag')

def CmdTB():
    print("Choix :")
    print("--------")
    print("Command Prompt (CMD): 0")
    print("Regedit (REG) : 1")
    print("PowerShell (PWSHELL): 2")
    print("Msinfo32 (MSINFO32): 3")
    print("Quit : 4")
    print("--------")
    
    ask=int(input("Votre choix : "))
    
    if ask == 0:
        os.system('start cmd')       
    if ask == 1:
        os.system('start regedit')        
    if ask == 2:
        os.system('start powershell')          
    if ask == 3:
        os.system('msinfo32')     
    if ask == 4:
        sys.exit(0)
    os.system('cls')

while True:
    CmdTB()
