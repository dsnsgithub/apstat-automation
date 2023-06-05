import pyautogui, time, win32gui
#? pip install pyautogui pywin32 opencv-python pillow

firstList = int(input("List #1: ") or 1)
secondList = int(input("List #2: ") or 2)
yStore = int(input("Store Line: ") or 1)
statPlot = int(input("Statplot Num: ") or 1)

cache = {}
def clickButton(image, conf=0.7):
    if image not in cache:
        coords = pyautogui.locateCenterOnScreen(image, confidence=conf, grayscale=True, region=region)
        cache[image] = coords

    pyautogui.moveTo(cache[image])
    pyautogui.mouseDown()
    time.sleep(0.001)
    pyautogui.mouseUp()

def chooseList(listNum):
    clickButton("2nd.PNG")
    clickButton("stat.PNG")
    pyautogui.typewrite(str(listNum))

print()
print("Waiting 1 seconds before entering....")
time.sleep(1)

# Bring CEMU window into focus
handle = win32gui.FindWindow(None, "CEmu | Calculator")
win32gui.SetForegroundWindow(handle)
region = win32gui.GetWindowRect(handle)

# Clear all y-vars
clickButton("y=.PNG")
clickButton("clear.PNG", 0.8)
for i in range(10):
    pyautogui.press("enter")
    pyautogui.mouseDown()
    time.sleep(0.001)
    pyautogui.mouseUp()

# Ensures the calculator is in stats mode
clickButton("stat.PNG")

# Navigate to LinReg
pyautogui.press("right")
pyautogui.typewrite("8") # selects LinReg(a+bx)

chooseList(firstList) # Enter List Number (L1)
pyautogui.press("down") 

chooseList(secondList) # Enter List Number (L2)
pyautogui.press("down")

# Move past FreqList
pyautogui.press("down") 

# Enter Y-Var
clickButton("vars.PNG")
pyautogui.press("right")
pyautogui.typewrite("1")
pyautogui.typewrite(str(yStore))

# Complete LinReg
pyautogui.press("down")
pyautogui.press("enter")

# Wait to continue
time.sleep(3)
input("Press enter to proceed...")

# Bring CEMU window into focus
win32gui.SetForegroundWindow(handle)

# Go to statplot
clickButton("2nd.PNG")
clickButton("y=.PNG")
pyautogui.typewrite(str(statPlot))
pyautogui.press("enter") # makes sure it is on

pyautogui.press("down")

# Place it in scatterplot mode (first option)
pyautogui.press("enter")
pyautogui.press("down")

chooseList(firstList) # Enter List Number (L1)
pyautogui.press("down")
chooseList(secondList) # Enter List Number (L2)

# Enter zoom and view graph
clickButton("zoom.PNG")
pyautogui.typewrite("9")
