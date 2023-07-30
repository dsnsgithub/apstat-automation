# AP Statistics Automation - Ti-84 Data Entry

This script automates the data entry process for the TI-84 calculator emulator (CEMU), which is very useful for AP Statistics homework. It reads input from a text file (`input.txt`) and enters the data into the emulator, saving time, eliminating mistakes, and making data entry easier.

## Prerequisites

Make sure you have the following dependencies installed before running the script:

-   `pyautogui`
-   `pywin32`
-   `opencv-python`
-   `pillow`

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

   - Make sure the keypad tab is clicked/visible

5. Take pictures of the calculator buttons, and place them in /images

   - The .png images will most likely not work on your computer, so screenshot each button and replace the files in /images
   - Please screenshot:
      - 2nd button (2nd.PNG)
      - clear button (clear.PNG)
      - stat button (stat.PNG)
      - vars button (vars.PNG)
      - y= button (y=.PNG)
      - zoom button (zoom.PNG)

6. Run the script by executing the following command:

    ```shell
    python main.py
    ```

7. The script will prompt you to choose between entering data by rows (1) or columns (2).

8. After selecting the data entry mode, the script will start entering the data into the CEMU emulator. It will perform the following steps:

    - Clean the input data by removing unwanted characters.
    - Bring the CEMU window into focus.
    - Ensure that the calculator is in stats mode.
    - Clear all lists in the emulator.
    - Enter the cleaned data into the emulator, one list at a time.

9. Wait for the script to complete. It will print the entered values on the console for verification.

**Note:** Make sure the CEMU emulator window with the title "CEmu | Calculator" is open and visible on your screen before running the script.

Feel free to customize the script by modifying the variables at the beginning of the script:

- `splitChar`: Specify the character used to separate data points in the input file.
- `regexAdditions`: Specify additional characters to include in the regular expression for cleaning the data.

## Using LinReg.py

1. Run the script as before, only changing the name of the file:

   ```shell
   python linreg.py
   ```

2. The script will prompt you to provide inputs for various parameters. The parameters and their default values are as follows:

   - `List #1`: Enter the number of the first list to be used in calculations (default: 1) - L1=1, L2=2, L3=3.
   - `List #2`: Enter the number of the second list to be used in calculations (default: 2) - L1=1, L2=2, L3=3.
   - `Store Line`: Enter the line number to store the results (default: 1) - Y1=1, Y2=2, Y3=3.
   - `Statplot Num`: Enter the number of the stat plot to display the graph (default: 1) - Plot1=1, Plot2=2, Plot3=3.

   You can press Enter for each parameter to accept the default values or enter your own values.

3. The script will start entering data and performing calculations in the CEMU emulator window. It will perform the following steps:

   - Clear all y-vars.
   - Ensure that the calculator is in stats mode.
   - Navigate to LinReg(a+bx) calculation.
   - Choose the specified list numbers for calculations.
   - Enter the specified store line number for results.
   - Perform the LinReg calculation.
   - Wait for a few seconds and prompt you to press Enter to proceed, allowing you to copy down the LinReg information.
   - Go to the stat plot configuration.
   - Choose the specified stat plot number.
   - Select scatterplot mode.
   - Choose the specified list numbers for the scatterplot.
   - Enter the zoom mode and view the graph.

4. Follow the prompts and wait for the script to complete its execution.

## Acknowledgments

Special thanks to the creators of [CEmu](https://github.com/CE-Programming/CEmu) for their invaluable contribution in making this project possible.
