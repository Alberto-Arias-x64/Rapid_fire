from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
import threading
import time

global teclastart
global botonmouse

teclastart=False
botonmouse=False

def on_click(x, y, button, pressed):
	global botonmouse
	tecla=str(button)
	if(tecla=="Button.left"):
		botonmouse= not botonmouse
		#print(botonmouse)

def on_press(key):
	global teclastart
	tecla=str(key)
	if(tecla=="'|'"):
		teclastart= not teclastart
		#print(teclastart)

def leermouse():
	with mouse.Listener(on_click=on_click) as c:
		c.join()

def leerteclado():
	with keyboard.Listener(on_press=on_press) as c:
		c.join()

def power():
	global teclastart
	global botonmouse
	mouse = Controller()
	while(1):
		if(teclastart and botonmouse):
			#print("puto \n")
			mouse.press(Button.left)
			time.sleep(0.025)
			mouse.release(Button.left)
			time.sleep(0.025)

hilo1=threading.Thread(target=leermouse)
hilo2=threading.Thread(target=leerteclado)
hilo3=threading.Thread(target=power)

hilo1.start()
hilo2.start()
time.sleep(5)
print("Ready")
hilo3.start()
