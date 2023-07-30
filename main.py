import pyautogui, time, re, win32gui

# ? pip install pyautogui pywin32 opencv-python pillow

inputFile = open("input.txt", "r").readlines()

#! Config
splitChar = " "  # ? change if necessary
regexAdditions = "-"  # ? change if necessary

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

for index, value in enumerate(clean):
    print(f"#{index + 1}:", value)
    print()

listsWanted = input("Enter the columns/rows you want to enter, seperated by spaces: ").split(" ")

print()

print("Waiting 2 seconds before entering....")
time.sleep(2)

# Bring CEMU window into focus
handle = win32gui.FindWindow(None, "CEmu | Calculator")

win32gui.SetForegroundWindow(handle)
win32gui.MoveWindow(handle, 100, 100, 1000, 1000, True)

region = win32gui.GetWindowRect(handle)

time.sleep(0.2)

# Ensures the calculator is in stats mode
statButtonCoords = pyautogui.locateCenterOnScreen(
    "./images/stat.PNG", confidence=0.7, grayscale=True, region=region
)
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
    pyautogui.typewrite("1")  # replaces entire field
    pyautogui.press("backspace")
    pyautogui.press("enter")
    pyautogui.press("left")
    pyautogui.press("up")


for index, column in enumerate(clean):
    if listsWanted.count(str(index + 1)) > 0:
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
