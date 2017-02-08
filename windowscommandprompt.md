## INTRO
In this file youll find some of commands that works for some shortcuts like; removing programs, and check the wifi passwords etc. 
 
`netsh wlan show profile name=#wifiname key=clear ` = it ill show the wifi features including sec. keys<br/>
`msiexec /x #program-name` = deletes program <br/>
```
WMIC
PRODUCT GET NAME
PRODUCT WHERE NAME="#YOURPROGRAMNAME"
PRODUCT WHERE NAME="#YOURPROGRAMNAME" call uninstall
#Afterthis, command prompt provide confirmation, type Y on that
```
= delete program on long way
