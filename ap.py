import pywhatkit
import keyboard
import time
from datetime import datetime

#numero de celular com DDD

contato = ['']

while len (contato) >= 1:

    pywhatkit.sendwhatmsg(contato[0],'mensagem', datetime.now().hour,datetime.now().
    minute + 2)
    del.contato[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')

