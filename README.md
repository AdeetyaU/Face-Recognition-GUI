# Face Recognition and Attendance Program GUI :memo:
![Face recog](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/face-recog.jpg)

##  For Command Line Interface Version, click [here](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program) (It runs faster than this, but it is a bit tricky to run it)

## Features :clipboard:

* Check Camera :camera:
* Capture Faces
* Train Faces
* Recognize Faces & Attendance
* Automatic Email :email:

## Tech Used :computer:

Build With -
* Python 3.8

Module Used -

All The Module are the Latest Version.
* OpenCV Contrib 4.0.1
* Pillow
* Numpy
* Pandas
* Shutil
* CSV
* yagmail
* PySimpleGUI


Face Recognition Algorithms -
* Haar Cascade
* LBPH (Local Binary Pattern Histogram)

Software Used -
* Pycharm 2020.2

## How to run :question:

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
  git clone https://github.com/AdeetyaU/Face-Recognition-GUI.git
  ```

#### 3. Now open this project on PyCharm and open terminal. Then enter the following commands:
---------------------------
```
python -m venv env
```
Then activate the enviroment using the code below (Works in CMD as well as PyCharm)

```
.\env\Scripts\activate
```
![venv](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/VENV.gif)

[ PS: If you have any issues with your venv, check this article then: (https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) ]

#### 4.1 Installing the packages
---------------------------
After creating the enviroment on your project let's install the necessary packages.

You simply need to run the following command in terminal, and it automatically installs the required packages for you:

```
py setup.py
```
![set up.py](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program/blob/master/README%20Images/setuppy.gif)

**If you get an error message, you need to manually install the package:**

#### 4.2 Installing the packages manually (ONLY IF STEP 4.1 DID NOT WORK)
---------------------------
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
```
pip install pysimplegui
```
After creating the enviroment and installing the packages, open the terminal to run the program. Using the code below.
```
py main.py
```
![GUI Interface](https://github.com/AdeetyaU/Face-Recognition-GUI/blob/master/README%20Images/Screenshot%202020-09-15%20124730.png)

#### 5. How to Set up the Attendance System?
---------------------------
###### This is a process that only needs to be done once for a user:

1. Click on Capture Face
2. Enter Id and Name and press Submit
3. Look into the Camera until the progress bar is completely. Then it will automatically close.
4. **Then click on Train Images. This is important to do; otherwise, it will result in multiple errors**

###### Now whenever you need to use the software, just:

5. Once the training is complete, you can now click on Attendance Mode
6. Once attendance is complete, just click *back to menu* to quit  and the Attendance will be saved!
7. (Optional) You can also auto-email this to a person, just don't forget to initially add your password and email id to the python file!
---------------------------

### And your GUI is good to go!

## Frequently Asked Question

###### 1. How do I close the camera windows?

*Answer: Press the 'x' key or press the respective buttons below them*


###### 2. Does it work with Linux/Mac ?

*Answer: A few commands in the program are Windows-Centric; however, I have not tested them yet in other Operating Systems. The CLI version of this works in both Linux and Mac. You can try it [here](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program)!*


###### 3. I can't install the required dependencies

*Answer: Try searching for unofficial dependencies and download them, then run CMD on that. Although this scenario is quite rare.*


###### 4. Where is the attendance saved?

*Answer: It is saved in the Attendance folder in a CSV format, you can open it using File > Open Attendance Folder in the GUI*


###### 5. Where is terminal in PyCharm?

*Answer: Check the lower left of your screen. Click on the Terminal button to open it up.*


###### 6. Why does it take time to load?

*Answer: This is written in python, therefore compiling it will take sometime depending on your computer's CPU speed!*


###### 7. How do I open the project once I unzip it?

*Answer: In PyCharm, click on File > Open Project > select Face-Recognition-Attendance-Program*


###### 8. Is a virtual environment necessary?

*Answer: No, however I highly recommend it.*


###### 9. Do I have to use Pycharm, can I use any other IDE?

*Answer: No it is not necessary, you can use VSCODE; however, I highly suggest using PyCharm for best results.*


###### 10. How can I suggest edits to the code?

*Answer: Make a pull request or raise an issue, and I'll get back to you as soon as possible!* :smiley:

#### Credits :gift_heart:
---------------------------
Thanks to [KMHMubin](https://github.com/kmhmubin/) for the initial source code ! This is an updated version of [my CLI based project](https://github.com/AdeetyaU/Face-Recognition-Attendance-Program) with the addition of a GUI for an easier accessibility and better looking interface!

## Next Update:
---------------------------
Making the loading time shorter :astonished:
