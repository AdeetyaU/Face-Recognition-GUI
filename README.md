# Face-Recognition-Attendance-Program :memo:
![Face recog](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/face-recog.jpg)

## Features :clipboard:
---------------------------
* Check Camera :camera:
* Capture Faces
* Train Faces
* Recognize Faces & Attendance
* Automatic Email :email:

## Tech Used :computer:
---------------------------
Build With -
* Python 3.8

Module Used -

All The Module are Latest Version.
* OpenCV Contrib 4.0.1
* Pillow
* Numpy
* Pandas
* Shutil
* CSV
* yagmail


Face Recognition Algorithms -
* Haar Cascade
* LBPH (Local Binary Pattern Histogram)

Software Used -
* Pycharm 2020.2

## How to run :question:
---------------------------
#### 1. Install PyCharm 2020.2 from [here](https://www.jetbrains.com/pycharm/download/) : https://www.jetbrains.com/pycharm/download/

![venv](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/pycharm.png)

#### 2. After installation:
---------------------------
  ##### Download or Clone the project:

  First Download or Clone the Project on Your Local Machine.To download the project from github press **_Download Zip_**

  ![save file](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/git%20save.png)

  **or**

  You can clone the project with git bash.To clone the project using git bash first open the git bash and write the following code
  ```
  git clone https://github.com/AdeetyaU/Face-Recognition-Attendance-Program.git
  ```

#### 3. Now open this project on PyCharm and open terminal. Then enter the following commands:
---------------------------
```
python -m venv env
```
Then activate the enviroment using the code below for windows.

```
.\env\Scripts\activate
```
![venv](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/VENV.gif)

[ PS: If you have any issues with your venv, check this article then: (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) ]

#### 4. Installing the packages
---------------------------
After creating the enviroment on your project let's install the necessary packages.

You simply need to run the following command in terminal, and it automatically installs the required packages for you:

```
py setup.py
```
![set up.py](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/setuppy.gif)

**If you get an error message, you need to manually install the package:**

![pip install demo](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/Pip%20install.gif)

To install those package open the terminal or command line and paste the code from below

```
pip install opencv-contrib-python
```
```
pip install numpy
```
```
pip install pandas
```
```
pip install Pillow
```
```
pip install pytest-shutil
```
```
pip install python-csv
```
```
pip install yagmail
```
After creating the enviroment and installing the packages, open the terminal to run the program. Using the code below.
```
py main.py
```
![main py](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/pymainpy.gif)

### And your program is good to go!

## Frequently Asked Question

###### 1. How do I close the camera window?

*Answer: Press the key **q** on your keyboard*


###### 2. Does it work with Linux/Mac ?

*Answer: Yes it does.*


###### 3. I can't install the required dependencies

*Answer: Try searching for unofficial dependencies and download them, then run CMD on that. Although this scenario is quite rare.*


###### 4. Where is the attendance saved?

*Answer: It is saved in the Attendance folder in a CSV format, you can open it using Excel*


###### 5. Where is terminal in PyCharm?

*Answer: Check the lower left of your screen. Click on the Terminal button to open it up.*


###### 6. Why does it take time to load?

*Answer: This is written in python, therefore compiling it will take sometime depending on your computer's CPU speed!*


###### 7. How do I open the project once I unzip it?

*Answer: In PyCharm, click on File > Open Project > select Face-Recognition-Attendance-Program*


###### 8. Is a virtual environment necessary?

*Answer: No, however I highly reccomend it.*


###### 9. Do I have to use Pycharm, can I use any other IDE?

*Answer: No it is not necessary, you can use VSCODE; however, I highly suggest using PyCharm for best results.*


###### 10. How can I suggest edits to the code?

*Answer: Make a pull request or raise an issue, and I'll get back to you as soon as possible!* :smiley:

#### Credits :gift_heart:
---------------------------
Thanks to [KMHMubin](https://github.com/kmhmubin/) for the initial source code ! This is an updated version of the FRAS project, with a stricter (and more accurate) face detection algorithm and multiple glitch fixes!

## Next Update:
---------------------------
Adding a GUI to make it look better :astonished:
