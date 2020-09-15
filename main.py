import os  # accessing the os functions
import Capture_Image
import Train_Image
import Recognize
import check_camera
import cv2
import PySimpleGUI as sg
import webbrowser as wb

def mainMenu():
    menu_def = [['&File', ['&Open Attendance Folder', '&Open Student Records','---', 'E&xit', ]],
                ['&Update', ['&Update Modules'], ],
                ['Help', ['Visit Repo','Creator','Version',"---",'Change Camera']], ]
    sg.theme('DefaultNoMoreNagging')
    #Design of the GUI
    layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
              [sg.Text('Face Recognition Attendance Program', font='Helvetica 36', justification = 'center')],
               [sg.Image(r'ReadME Images\face-recog.png', size=(660,480)) , sg.Image(filename='', key='image')],
                [sg.Button("Attendance Mode", size=(122, 2), font='Helvetica 14', button_color=('black', 'white'))],
               [ sg.Button("Capture Face", size=(60, 2), font='Helvetica 14', button_color=('black', 'white')), sg.Button("Train Images", size=(60, 2), font='Helvetica 14', button_color=('black', 'white'))],
               [sg.Button("AutoMail", size=(60, 2), font='Helvetica 14', button_color=('black', 'white')), sg.Button("Quit", size=(60, 2), font='Helvetica 14', button_color=('white', 'red'))] ]
    window = sg.Window('Face Attendance Recognition Program', layout,auto_size_buttons=False, element_justification='c')
    faceCascade,recognizer,df,minW,minH,font,cam= check_camera.initialize()
    #Buttons and Menu
    while True:
        event, values = window.read(timeout=1)
        if event == "Quit" or event == "Exit" or event == sg.WIN_CLOSED:
            cam.release()
            cv2.destroyAllWindows()
            window.close()
            break
        elif event == "Open Attendance Folder":
            path = "Attendance"
            path = os.path.realpath(path)
            os.startfile(path)
        elif event =="Open Student Records":
            path = "StudentDetails"
            path = os.path.realpath(path)
            os.startfile(path)
        elif event =="Update Modules":
            sg.popup_timed("The Main Menu may be unresponsive during this process. It will automatically come back online, once the process is finished")
            os.system("py setup.py")
        elif event =="Visit Repo":
            wb.open("https://github.com/AdeetyaU/Face-Recognition-Attendance-Program")
        elif event =="Creator":
            wb.open("https://github.com/AdeetyaU")
        elif event == "Version":
            window.disappear()
            sg.popup('Face Attendance Recognition Program', 'Version 1.1',
                     'GUI Version: ', sg.version, grab_anywhere=True)
            window.reappear()
        elif event == "Capture Face":
            cam.release()
            cv2.destroyAllWindows()
            window.close()
            Capture_Image.takeImages()
            mainMenu()
            break
        elif event == "Train Images":
            window.close()
            Train_Image.TrainImages()
            mainMenu()
            break
        elif event == "Attendance Mode":
            window.close()
            Recognize.recognize_attendence()
            mainMenu()
            break
        elif event == "AutoMail":
            window.close()
            os.system("py automail.py")
            mainMenu()
            break
        im = check_camera.cam(faceCascade,recognizer,df,minW,minH,font,cam)
        im = cv2.copyMakeBorder(im, 2, 2, 2, 2, cv2.BORDER_CONSTANT)
        imgbytes = cv2.imencode(".png", im)[1].tobytes()
        window["image"].update(data=imgbytes)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
mainMenu()
