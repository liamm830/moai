import sys
import time

def printi(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def start():
    printi("the 🗿🗿🗿 rises above the 🗿🗿🗿🗿🗿🗿🗿 as the 🗿🗿🗿🗿🗿🗿🗿🗿 🗿🗿🗿🗿 \n")
printi("but 🗿🗿🗿 🗿🗿🗿🗿 ever going to 🗿🗿🗿🗿 \n")
printi("In 🗿🗿🗿🗿🗿 the outcast 🗿🗿🗿🗿 lives, its name is 🗿🗿🗿🗿🗿 \n")

def death():
    printi("the sun rises above the horizon as the roosters crow, but are they ever going to stop? In Japan the outcast Moai lives, its name is moyai \n")
    play()

def play():
    printi("test")