# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xy9hGLqqNy7rTv9WikqU1xilBrHYgmfS

PRACTICA PYTHON IE
"""

print("Daniel Amo Navas")

print("Daniel Amo Navas, Española, Estudiante")

print("Daniel")
print("Española")
print("Estuidante")

print("Daniel Amo Navas\n", "Española\n", "Estudiante\n")

x=4
print(x)

y=1
print(y)

string_value = "Hola Mundo"
boolean_value = bool(string_value)
print(boolean_value)

# Python code to demonstrate
# to convert boolean value to integer
 
# Initialising Values
bool_val = True
  
# Printing initial Values
print("Initial value", bool_val)
  
# Converting boolean to integer
bool_val = int(bool_val == True)
 
# Printing result
print("Resultant value", bool_val)

#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)

new_date = datetime(1986, 2, 16, 10, 15, 00, 00000)
print(new_date)