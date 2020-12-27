from menu_based import*
from console_based import*
print("1.Menu-based")
print("2.Console-based")
command=int(input("Which option would you like to choose:"))
if(command==1):
    print("")
    startMenuBased()
else:
    print("")
    startConsoleBased()
