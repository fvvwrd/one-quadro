import PySimpleGUI as sg
from math import *

sg.theme('SandyBeach')
layout = [
          [sg.Text('Решение системы квадратных уравнений')],
          [sg.Text('a = '), sg.InputText(size=(5,1)),
           sg.Text('b = '), sg.InputText(size=(5,1)),
           sg.Text('c = '), sg.InputText(size=(5,1))],
        
          [sg.Text('x = '), sg.InputText(size=(5,1), key='x'),
           sg.Text('y = '), sg.InputText(size=(5,1), key='y')],
          [sg.Button('Ok'), sg.Button('Exit'),sg.Button('Clear')]
          ]

window = sg.Window('Решение квадратных уравнений', layout,
                   location = (0,0),
                   size = (500,350),
                   margins = (25,25),
                   element_padding = (10,10),
                   font = 'Verdana',
                   element_justification = "center")

while True:
    event, values = window.read()
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        a = float(values[0])
        print(a)
        b = float(values[1])
        c = float(values[2])
        print(values)
        
        d = b*b-4*a*c
        #x = (-b+sqrt(d))/2*a
        #y = (-b-sqrt(d))/2*a
        
        if d == 0.0:
            x = y = '∞'
        elif d<0.0:
            x = y = 'None'
        else:
            x = (-b+sqrt(d))/2*a
            y = (-b-sqrt(d))/2*a
        print('x:',x,'y:',y)
        window["x"].update(x)
        window["y"].update(y)
window.close()
