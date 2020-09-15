import yagmail
import os
import datetime
import PySimpleGUI as sg
sg.theme('DefaultNoMoreNagging')
layout = [[sg.Text('Recipient:', size =(15, 1)), sg.InputText()],
          [sg.Text('Message:', size =(15, 1)), sg.InputText()],
          [sg.Button('Submit'), sg.Button('Cancel'), sg.Button('Default Settings')]]

window = sg.Window('AutoMail', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        window.close()
        break
    elif event == 'Submit':
        receiver = values[0]
        body = values[1]
        window.close()
    elif event == 'Default Settings':
        receiver = "amazingadeetya88@gmail.com"
        body = "Attendance for Today"
        window.close()

date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("amazingadeetya88@gmail.com", "jlztweareoswptim")

# sent the mail
yag.send(
    to=receiver,
    subject=sub, # email subject
    contents=body,  # email body
    attachments= filename  # file attached
)
sg.popup_auto_close("Email Sent!")
