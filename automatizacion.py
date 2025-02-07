import pyautogui
import time

pyautogui.moveTo(100, 200, duration=1)  # Mueve el mouse a (100, 200) en 1 segundo
pyautogui.click()  # Hace clic en la posición actual

pyautogui.write("Hola, esto es una prueba", interval=0.1)  # Escribe letra por letra con 0.1s de pausa
pyautogui.press("enter")  # Presiona Enter

screenshot = pyautogui.screenshot()
screenshot.save("captura.png")  # Guarda la captura como archivo

x, y = pyautogui.position()  # Obtiene las coordenadas actuales del cursor
print(f"El mouse está en: {x}, {y}")


pyautogui.hotkey("win", "r")  # Abre el "Ejecutar" de Windows
time.sleep(1)
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(2)
pyautogui.write("Hola, este mensaje fue escrito automáticamente!", interval=0.1)

#Automatización de tareas repetitivas en el PC
#Pruebas automáticas de software (UI Testing)
#Simulación de teclas y clics en juegos o aplicaciones
#Automatización de llenado de formularios