flnm = str(input("Enter file name to run:\n"))
import os
import random
import time
import pyautogui
import webbrowser
import math


def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""

#####---CATCHING FILENOTFOUND ERROR---#####
try:
    with open(flnm,'r') as file:
        contents = file.read()
        contents = contents.strip()
        

except(FileNotFoundError):
    print("\n\033[31m\033[1m\033[4m"+flnm+"\033[0m")
    print("\033[31m\033[1m^"*len(flnm)+"\n")
    print("\033[31m\033[1m\033[4m'"+flnm+"' File not found in working directory.\033[0m")
    print("\033[35m\033[1m\033[4mHelp: Try changing working directory to the location of your file or drag the file into your working directory\033[0m\n")
try:
    contents = contents.splitlines()
except(NameError):
    exit()



    

def anal():
    

    idx = item.split("(")[0]



    if idx == "push":
        actual = eval(find_between(item,"(",")")) 
        print((actual))
    if idx == "class":
        actual = eval(find_between(item,"(",")"))
        print(type(actual))

    if idx == "alc":
        actual2 = (find_between(item,"(",")"))
        val = (find_between(item,"{","}"))
        globals()[actual2] = val
        if "pull(" in val:
            actual3 = eval(find_between(item,"pull(",")"))
            globals()[actual2] = input(actual3)
        if "random(" in val:
            actual3 = eval(find_between(item,"random(",")"))
            globals()[actual2] = random.randint(0,actual3)
        
    
    if idx == "tostr":
        actual = (find_between(item,"(",")"))
        globals()[actual] = str(globals()[actual])
    if idx == "toint":
        actual = (find_between(item,"(",")"))
        globals()[actual] = int(globals()[actual])
    if idx == "up":
        actual = (find_between(item,"(",")"))
        globals()[actual] = globals()[actual].upper()
    if idx == "low":
        actual = (find_between(item,"(",")"))
        globals()[actual] = globals()[actual].lower()
    if idx == "opentab":
        actual = eval(find_between(item,"(",")"))
        webbrowser.open_new_tab(actual)
    if idx == "mkfolder":
        actual = eval(find_between(item,"(",")"))
        actual = actual.strip()
        os.system("mkdir "+actual)
    
        
    if idx == "toflt":
        actual = (find_between(item,"(",")"))
        globals()[actual] = float(globals()[actual])
    if idx == "totupl":
        actual = (find_between(item,"(",")"))
        globals()[actual] = tuple(globals()[actual])
    if idx == "random":
        actual = eval(find_between(item,"(",")"))
        print(random.randint(0,actual))
    
    if idx == "random!":
        actual = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            print(random.randint(0,actual))


    if idx == "random_range":
        actual = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        print(random.randint(actual,val))
    if idx == "msg":
        actual = eval(find_between(item,"(",")"))
        os.system("msg * "+actual)
    
    if idx == "wait":
        actual = eval(find_between(item,"(",")"))
        time.sleep(actual)
    if idx == "pull":
        actual = eval(find_between(item,"(",")"))
        input(actual)
    if idx == "start":
        actual = eval(find_between(item,"(",")"))
        os.system("start "+actual)
    if idx == "is":
        actual = eval(find_between(item,"(",")"))
        print(actual)
    
    if idx == "castro":
        print("""\033[95m\033[1m\033[4m

░█████╗░░█████╗░░██████╗████████╗██████╗░░█████╗░
██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║╚█████╗░░░░██║░░░██████╔╝██║░░██║
██║░░██╗██╔══██║░╚═══██╗░░░██║░░░██╔══██╗██║░░██║
╚█████╔╝██║░░██║██████╔╝░░░██║░░░██║░░██║╚█████╔╝
░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░""")
        print("\033[95m\033[1m\033[4mCastro")
        print("V/0.3")
        print("First Release")
        print()
        print("Dev: CmSpeedrunner\033[0m")
####---Configuring color selection---###
    if idx == "green+":
        print("\033[0;32m")
        print("\033[1A\033[2K", end="")
    if idx == "purple+":
        print("\033[0;95m")
        print("\033[1A\033[2K", end="")
    if idx == "red+":
        print("\033[0;31m")
        print("\033[1A\033[2K", end="")
    if idx == "black+":
        print("\033[0;30m")
        print("\033[1A\033[2K", end="")
    if idx == "yellow+":
        print("\033[0;33m")
        print("\033[1A\033[2K", end="")
    if idx == "blue+":
        print("\033[0;34m")
        print("\033[1A\033[2K", end="")
    if idx == "cyan+":
        print("\033[0;36m")
        print("\033[1A\033[2K", end="")

    if idx == "underline+":
        print("\033[4m")
        print("\033[1A\033[2K", end="")
    if idx == "bold+":
        print("\033[1m")
        print("\033[1A\033[2K", end="")
    if idx == "italic+":
        print("\033[3m")
        print("\033[1A\033[2K", end="")

    if idx == "format-":
        print("\033[0m")
        print("\033[1A\033[2K", end="")
####---Configuring MachControl---###
    if idx == "moveto":
        dur = eval(find_between(item,"(",")"))
        x = eval(find_between(item,"){","}{"))
        y = eval(find_between(item,"}{","}"))
        pyautogui.moveTo(x, y, duration=dur)
    if idx == "lmb":
        pyautogui.click()
    if idx == "rmb":
        pyautogui.rightClick()
    if idx == "type":
        dur = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        pyautogui.typewrite(dur, interval=val)
    if idx == "press":
        dur = eval(find_between(item,"(",")"))
        pyautogui.press(dur)
    if idx == "release":
        dur = eval(find_between(item,"(",")"))
        pyautogui.keyUp(dur)
    if idx == "scroll":
        dur = eval(find_between(item,"(",")"))
        pyautogui.scroll(dur)
    if idx == "screenshot":
        dur = eval(find_between(item,"(",")"))
        pyautogui.screenshot(dur)
    if idx == "find_click":
        dur = eval(find_between(item,"(",")"))
        button_location = pyautogui.locateOnScreen(dur)
        pyautogui.moveTo(button_location)
        pyautogui.click()
    if idx == "dragto":
        pyautogui.mouseDown()
        dur = eval(find_between(item,"(",")"))
        x = eval(find_between(item,"){","}{"))
        y = eval(find_between(item,"}{","}"))
        pyautogui.moveTo(x, y, duration=dur)
        pyautogui.mouseUp()
        
    if idx == "circle":

        center_x, center_y = 500, 500
        radius = 100

    # Move the mouse to the center point of the circle and press down the left button
        pyautogui.moveTo(center_x, center_y)
        

    # Calculate the points of the circle and move the mouse to each point
        for i in range(0, 361, 10):
            x = center_x + int(radius * math.cos(math.radians(i)))
            y = center_y + int(radius * math.sin(math.radians(i)))
            pyautogui.moveTo(x, y, duration=0.0002)
            pyautogui.mouseDown()

    # Release the left button to finish the circle drawing
        pyautogui.mouseUp()
####---Configuring Macros---####

    if idx == "msg!":
        actual = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            os.system("msg * "+actual)
    if idx == "random!":
        actual = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            print(random.randint(0,actual))
    if idx == "opentab!":
        actual = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            webbrowser.open_new_tab(actual)
    if idx == "push!":
        actual = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            print(actual)

    if idx == "moveto!":
        dur = eval(find_between(item,"(",")"))
        x = eval(find_between(item,"){","}{"))
        y = eval(find_between(item,"}{","}"))
        times = eval(find_between(item,"{","}"))
        for i in range(times):
            pyautogui.moveTo(x, y, duration=dur)
    if idx == "lmb!":
        ur = eval(find_between(item,"{","}"))
        for i in range(ur):
            pyautogui.click()
    if idx == "rmb!":
        ur = eval(find_between(item,"{","}"))
        for i in range(ur):
            pyautogui.rightClick()
    if idx == "type!":
        dur = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        ur = eval(find_between(item,"}{","}"))
        for i in range(ur):
            pyautogui.typewrite(dur, interval=val)
    if idx == "press!":
        dur = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            pyautogui.press(dur)
    if idx == "release!":
        dur = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            pyautogui.keyUp(dur)
    if idx == "scroll!":
        dur = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            pyautogui.scroll(dur)
    if idx == "screenshot!":
        dur = eval(find_between(item,"(",")"))
        val = eval(find_between(item,"{","}"))
        for i in range(val):
            pyautogui.screenshot(dur)

for i, item in enumerate(contents):
    anal()
