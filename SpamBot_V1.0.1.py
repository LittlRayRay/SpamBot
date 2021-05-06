import PySimpleGUI as sg
import pyautogui 
import time 


sg.theme("SandyBeach")

layout = [ 
    [sg.Text('Please enter how many times to spam and what to spam:')], 
    [sg.Text('Times To Spam', size =(15, 1)), sg.InputText()], 
    [sg.Text('What To Spam', size =(15, 1)), sg.InputText()],
    [sg.Text('Please note: after you press submit, you will have 5 seconds')],
    [sg.Text('to move to Whatsapp, Discord etc.')], 
    [sg.Submit(), sg.Cancel()] 
] 


# Create the window
window = sg.Window('Spam Bot v1.0.0', layout) 
event, values = window.read() 
window.close() 


 
#print(event, values[0], values[1])



beforeIntifying = int(values[0])
numberOfTimesToSpam = beforeIntifying
WhatToSpam = values[1]
time.sleep(5)
while numberOfTimesToSpam >= 0:
	pyautogui.typewrite(WhatToSpam)
	pyautogui.press("enter")
	numberOfTimesToSpam -= 1


while True:
	if event == sg.WIN_CLOSED or event == sg.Cancel:
		break

# Create an event loop
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED:
		break


window.close()