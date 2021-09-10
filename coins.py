# Interface gráfica utilizando o PySimpleGUI para pegar a cotação de moedas
from math import comb
from PySimpleGUI import PySimpleGUI as sg
import xml.etree.ElementTree as et 
import requests

# Request
# request = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
# print(request.content);

def arrayCode(root):
    coinsCode = []
    for child in root:
        coinsCode.append(child.tag)
    return coinsCode
    
def arrayName(root):
    coinsName = []
    for child in root: 
        coinsName.append(child.text)
    return coinsName


def main():
    # Read xml with UTF8
    with open('listCodeCoins.xml', 'r') as xml_file:
        root = xml_tree = et.parse(xml_file).getroot()

    coinsCode = arrayCode(root)
    coinsName = arrayName(root)

    # Layout
    sg.theme('Reddit')
    width = max(map(len, coinsName))+1
    layout = [
        [sg.Text('Moeda'), sg.Combo(coinsName, size=(width, 8), enable_events=True, key='moeda1')],
        [sg.Text('Moeda'), sg.Combo(coinsName, size=(width, 8), enable_events=True, key='moeda2')],
        [sg.Button('Vamos lá!', key='go')],
    ]

    # Window
    window = sg.Window('Conversor de Moedas', layout)

    # Read events
    while True:
        events, values = window.read()
        if events == sg.WINDOW_CLOSED:
            break
        if events == 'go':
            combo = values['moeda1']
            print(combo)

if __name__ == '__main__':
    main()