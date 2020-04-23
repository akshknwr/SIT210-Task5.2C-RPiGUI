import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QRadioButton, QMainWindow, QGridLayout, QVBoxLayout, QWidget
import sys
from PyQt5.QtCore import QRect
import functools

red=8   #defining red led pin 
blue=31 #defining blue led pin 
green=33 #defining green led pin 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)

def radioSelected(ledcolor):
    print(ledcolor)
    if(ledcolor=="green"):
     
        GPIO.output(green,GPIO.HIGH)
        GPIO.output(red,GPIO.LOW)
        GPIO.output(blue,GPIO.LOW)
    elif(ledcolor=="blue"):
      
        GPIO.output(green,GPIO.LOW)
        GPIO.output(red,GPIO.LOW)
        GPIO.output(blue,GPIO.HIGH)
    elif(ledcolor=="red"):
     
        GPIO.output(green,GPIO.LOW)
        GPIO.output(red,GPIO.HIGH)
        GPIO.output(blue,GPIO.LOW)



    
  
app=QApplication(sys.argv)
window = QWidget()
window.resize(800,600)
window.setWindowTitle("Rpi -GUI")
layout =QVBoxLayout()
btn = QPushButton('Exit')

greenRadio=QRadioButton("Green")
redRadio=QRadioButton("Red")
blueRadio=QRadioButton("Blue")

greenRadio.clicked.connect(functools.partial(radioSelected,'green'))
redRadio.clicked.connect(functools.partial(radioSelected,'red'))
blueRadio.clicked.connect(functools.partial(radioSelected,'blue'))
btn.clicked.connect(QApplication.instance().quit)

layout.addWidget(greenRadio)
layout.addWidget(redRadio)
layout.addWidget(blueRadio)
layout.addWidget(btn)
msg =QLabel('')
layout.addWidget(msg)

window.setLayout(layout)
window.show()
sys.exit(app.exec())






  
