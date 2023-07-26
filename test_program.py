import ezui
import sys

banner = """
  ______     _    _ _____ 
 |  ____|   | |  | |_   _|
 | |__   ___| |  | | | |  
 |  __| |_  / |  | | | |  
 | |____ / /| |__| |_| |_ 
 |______/___|\____/|_____|
                          
"""

def add(a, b):
    return a + b

def say_hello():
    print("Hello World!")

def sub(a, b):
    return a - b

def exit():
    sys.exit()

elements = [
    ("Hello World Function",say_hello),
    ("Additionner", add),
    ("Sub two operands", sub),
    ("Exit the programm", exit)
]

ezui.simple_menu(elements, banner, "default")
