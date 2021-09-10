# Interface gráfica utilizando o PySimpleGUI para pegar a cotação de moedas
from math import comb
from PySimpleGUI import PySimpleGUI as sg
import xml.etree.ElementTree as et 
import requests
import json
import sys

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

def findName(selected, coinsName):
    # Find name in list of coins
    position = -1
    for index, aux in enumerate(coinsName):
        if(selected == aux):
            position = index
    print('selected: ', selected, 'in position ',  position)
    return position
    
def findCode(position, coinsCode):
    # Find code in list of coins
    return coinsCode[position]

def doRequest(code1, code2):
    # Receive code1 e code2 e assemble the request
    link = 'https://economia.awesomeapi.com.br/last/'
    finalLink = link + code1 + '-' + code2
    
    request = requests.get(finalLink)
    print(finalLink);
    result = request.json()
    try:
        print(result[code1 + code2]['bid'])
        return result[code1 + code2]['bid']
    except:
        return None

def main():
    # Read xml with UTF8
    with open('listCodeCoins.xml', 'r') as xml_file:
        root = et.parse(xml_file).getroot()

    coinsCode = arrayCode(root)
    coinsName = arrayName(root)

    # Layout
    sg.theme('Reddit')
    width = max(map(len, coinsName))+1
    layout = [
        [sg.Text('Moeda'), sg.Combo(coinsName, size=(width, 8), enable_events=True, key='coin1')],
        [sg.Text('Moeda'), sg.Combo(coinsName, size=(width, 8), enable_events=True, key='coin2')],
        [sg.Text('', key='result')],
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
            coin1 = findName(values['coin1'], coinsName)
            coin2 = findName(values['coin2'], coinsName)
            code1 = findCode(coin1, coinsCode)
            code2 = findCode(coin2, coinsCode)
            result = doRequest(code1, code2)
            if(result is None):
                message = 'Não foi possível buscar o valor digitado!'
            else:
                message = 'Um ' + values['coin1'] + ' vale ' + str(result) + ' ' + values['coin2']

            window.Element('result').Update(message)

if __name__ == '__main__':
    main()