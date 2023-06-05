# AP Statistics Automation - Ti-84 Data Entry

This script automates the data entry process for the TI-84 calculator emulator (CEMU), useful for AP Statistics homework. It reads input from a text file (`input.txt`) and enters the data into the emulator, saving time, eliminating mistakes, and making data entry easier.

## Prerequisites

Make sure you have the following dependencies installed before running the script:

- `pyautogui`
- `pywin32`
- `opencv-python`
- `pillow`

You can install these dependencies by running the following command:

```shell
pip install pyautogui pywin32 opencv-python pillow
```

## Usage

1. Clone this repository
```shell
git clone https://github.com/dsnsgithub/apstat-automation
cd apstat-automation
```

2. Place your input data in a text file named `input.txt` in the same directory as the script. This can be easily done by copy-pasting the charts from the AP Statistics homework PDF.

3. Open a command prompt or terminal in the script's directory.

4. Run CEmu.exe (emulator of choice)

   - Open File Explorer.
   - Go to the cloned repository folder.
   - Enter the /emulator folder.
   - Double-click/open CEmu.exe.
   - Close any extra popups. 

5. Run the script by executing the following command:

   ```shell
   python main.py
   ```

6. The script will prompt you to choose between entering data by rows (1) or columns (2).

7. After selecting the data entry mode, the script will start entering the data into the CEMU emulator. It will perform the following steps:

   - Clean the input data by removing unwanted characters.
   - Bring the CEMU window into focus.
   - Ensure that the calculator is in stats mode.
   - Clear all lists in the emulator.
   - Enter the cleaned data into the emulator, one list at a time.

8. Wait for the script to complete. It will print the entered values on the console for verification.

**Note:** Make sure the CEMU emulator window with the title "CEmu | Calculator" is open and visible on your screen before running the script.

Feel free to customize the script by modifying the variables at the beginning of the script:

- `splitChar`: Specify the character used to separate data points in the input file.
- `regexAdditions`: Specify additional characters to include in the regular expression for cleaning the data.


## Acknowledgments

Special thanks to the creators of [CEmu](https://github.com/CE-Programming/CEmu) for their invaluable contribution in making this project possible.
