import time
import datetime
import random

# Define a function to convert celsius to fahrenheit.
def c_to_f(c):
	return c * 9.0 / 5.0 + 32.0

def get_datetime():
    return datetime.datetime.now()

def get_temperature():
    temp = random.randint(1, 100)
    return temp
