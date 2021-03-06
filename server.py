from m5stack import *
from m5ui import *
from uiflow import *
from machine import Pin
import network
import wifiCfg
import usocket as socket

wifiCfg.doConnect('Pardal', 'brp79501')
wait_ms(2000)


lcd.setRotation(2)

setScreenColor(0x000000)

relay1 = Pin(2, Pin.OUT)
relay2 = Pin(19, Pin.OUT)

relay1.value(1)
relay2.value(1)

sta_if = network.WLAN(network.STA_IF)

TecPy = M5Title(title=str(sta_if.ifconfig()[0]), x=10 , fgcolor=0xffffff, bgcolor=0x33ec00)
circle0 = M5Circle(127, 123, 25, 0xFFFFFF, 0xFFFFFF)
triangle1 = M5Triangle(128, 211, 97, 162, 158, 162, 0xFFFFFF, 0xFFFFFF)
label0 = M5TextBox(42, 240, "tecpy.com.br", lcd.FONT_DejaVu24,0xFFFFFF, rotate=0)
triangle0 = M5Triangle(126, 34, 96, 85, 156, 85, 0xFFFFFF, 0xFFFFFF)

def auxBtnA():
  triangle0.setBgColor(0x33ff33)
  circle0.setBgColor(0xffffff)
  triangle1.setBgColor(0xffffff)
  relay1.value(1)
  relay2.value(0)
  pass


def buttonA_wasPressed():
  auxBtnA()
  pass
btnA.wasPressed(buttonA_wasPressed)




def auxBtnB():
  triangle0.setBgColor(0xffffff)
  circle0.setBgColor(0x33ff33)
  triangle1.setBgColor(0xffffff)
  relay1.value(1)
  relay2.value(1)
  pass


def buttonB_wasPressed():
  auxBtnB()
  pass
btnB.wasPressed(buttonB_wasPressed)




def auxBtnC():
  triangle0.setBgColor(0xffffff)
  circle0.setBgColor(0xffffff)
  triangle1.setBgColor(0x33ff33)
  relay1.value(0)
  relay2.value(1)
  pass

def buttonC_wasPressed():
  auxBtnC()
  pass
btnC.wasPressed(buttonC_wasPressed)




triangle0.setBgColor(0xffffff)
triangle1.setBgColor(0xffffff)
triangle0.setBorderColor(0xff0000)
triangle1.setBorderColor(0xff0000)
circle0.setBgColor(0x33ff33)
circle0.setBorderColor(0xff0000)


meu_host = '0.0.0.0'
minha_porta = 50007

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sockobj.bind((meu_host, minha_porta))

sockobj.listen(5)

while True:
  try:
    
    conexao, endereco = sockobj.accept()
    
    while True:
      data = conexao.recv(1024)
      if not data:
        break
      
      if (b''+data == b'a'):
        conexao.send(b'A')
        auxBtnA()
        wait_ms(1000)
        pass
      elif (b''+data == b'b'):
        conexao.send(b'B')
        auxBtnB()
        wait_ms(1000)
        pass
      elif (b''+data == b'c'):
        conexao.send(b'C')
        auxBtnC()
        wait_ms(1000)
        pass
      else:
        conexao.send(b'CU'+data)
        
    conexao.close()
      
  except:
    pass
  wait_ms(2)
  
  
  
  
  
  


