# EzUI
A python module for easily creating a powerful and dynamic user interface in windows shell

![](https://github.com/Plunder283/ezui/blob/main/readme_assets/ui_exemple.png)

## How to use:

Here is a simple program who use it : (You can find it in the repo)
```python
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

# This is the Menu elements
elements = [
    ("Hello World Function",say_hello),
    ("Additionner", add),
    ("Sub two operands", sub),
    ("Exit the programm", exit)
]

ezui.simple_menu(elements, banner, "default")
```

## Todo
    - Create a title system ✅
    - Find a way to know if the app is in foreground ❌
    - Find a way to handle key strokes on Linux ❌
