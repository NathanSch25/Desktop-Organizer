
import pygetwindow as gw
import subprocess
import pyautogui
import time

pyautogui.FAILSAFE = False
def MoveLeft(title):
    # Get the window's current position
    x, y = title.topleft
    # Calculate the new position where you want to move the window
    new_x = x - 960
    new_y = y
    # Move the window to the new position
    title.moveTo(new_x, new_y)
    time.sleep(1)
def FileOpen(address, title, w, h, x, y):
    subprocess.Popen([address])
    time.sleep(2)
    title1 = gw.getWindowsWithTitle(title)[0]  
    title1.resizeTo(w, h)  # width, height
    title1.moveTo(x, y)
    time.sleep(1)

adressEdge = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
adressSpot = 'C:\\Users\\sheeny525\\AppData\\Roaming\\Spotify\\Spotify.exe'
adressOutL = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\OUTLOOK.EXE'

FileOpen(adressEdge, 'Edge', 960, 1080, 0, 0)
FileOpen(adressSpot, 'Spotify', 960, 500, 0, 454)
FileOpen(adressOutL, 'Outlook', 960, 500, 0, 0)

spot = gw.getWindowsWithTitle('Spotify')[0]
MoveLeft(spot)
x, y = spot.topleft
pyautogui.moveTo(x + 480, y + 535)
pyautogui.click()

outL = gw.getWindowsWithTitle('Outlook')[0]
MoveLeft(outL)
