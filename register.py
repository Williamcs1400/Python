# Interface gráfica utilizando o PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='user', size=(20, 0))],
    [sg.Text('Senha'), sg.Input(key='password', password_char='*', size=(20, 0))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]

# Window
window = sg.Window('Tela De Login', layout)

# Read events
while True:
    events, values = window.read()
    if events == sg.WINDOW_CLOSED:
        break
    if events == 'Entrar':
        if values['user'] == 'will' and values['password'] == 'coelho':
            print('Bem vindo will')