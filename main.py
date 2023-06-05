import pyautogui, time, re, win32gui
#? pip install pyautogui pywin32 opencv-python pillow

inputFile = open("input.txt", "r").readlines()

#! Config
splitChar = " "  # ? change if necessary
regexAdditions = "-" # ? change if necessary

regex = f"[^0-9\s.{regexAdditions}]"

choice = int(input("Rows (1) / Columns (2): "))

clean = []
if choice == 1:
    for line in inputFile:
        cleanLine = re.sub(regex, "", line).strip()
        lineList = cleanLine.split(splitChar)
        for index, num in enumerate(lineList):
            if num.startswith("-"):  # fix negatives
                lineList[index] = "0" + num
        clean.append(lineList)
else:
    for line in inputFile:
        cleanLine = re.sub(regex, "", line).strip()
        lineList = cleanLine.split(splitChar)
        for columnNum, num in enumerate(lineList):
            if columnNum >= len(clean):  # expands the array to match any # columns
                clean.append([])

            if num.startswith("-"):  # fix negatives
                num = "0" + num

            clean[columnNum].append(num)

for value in clean:
    print(value)
print()

print("Waiting 1 seconds before entering....")
time.sleep(1)

# Bring CEMU window into focus
handle = win32gui.FindWindow(None, "CEmu | Calculator")
win32gui.SetForegroundWindow(handle)
region = win32gui.GetWindowRect(handle)

# Ensures the calculator is in stats mode
statButtonCoords = pyautogui.locateCenterOnScreen("stat.PNG", confidence=0.7, grayscale=True, region=region)
print(statButtonCoords)

pyautogui.moveTo(statButtonCoords)
pyautogui.mouseDown()
time.sleep(0.01)
pyautogui.mouseUp()
pyautogui.press("enter")

# Clear all lists
pyautogui.press("down")
for i in range(6):
    pyautogui.press("right")
pyautogui.press("up")
for i in range(6):
    pyautogui.press("enter")
    pyautogui.typewrite("1") # replaces entire field
    pyautogui.press("backspace")
    pyautogui.press("enter")
    pyautogui.press("left")
    pyautogui.press("up")


for index, column in enumerate(clean):
    payload = "{"
    for num in clean[index]:
        payload += str(num)
        payload += ","
    payload = payload[:-1]  # removes trailing comma
    payload += "}"

    pyautogui.typewrite(payload)

    # Move to next List
    pyautogui.press("enter")
    pyautogui.press("right")
    pyautogui.press("up")
    pyautogui.press("enter")
