import os 
from uuid import uuid4
from time import sleep

while True:
    os.makedirs(str(uuid4()))
    sleep(600)