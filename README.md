# Raspberry Pi ISS Pointer

Dev: djgood@github.com  
Dev: k4yt3x@github.com  
Date Created: Dec 16, 2017  
Last Modified: jan 16, 2017  

## Current Version: 0.2 alpha

## Change Logs:
1. Added main controller
1. Fixed motor controller
1. Project Imported

## Description
The raspberry pi ISS Pointer is a simple device that will always point to the current location of the International Space Station (ISS).
This project is initialized as an ISU project.

## Usage
Setup the hardware according to the tho graphs below
Then execute:
~~~~
$ git clone https://github.com/K4YT3X/ISS-Pointer.git
$ cd ISS-Pointer
$ sudo python3 isspointer.py
~~~~

## GPIO Header
![pi3_gpio](https://user-images.githubusercontent.com/21986859/34141154-78ec6628-e44d-11e7-8ef6-7ffcb87f79a1.png)
![isspinsetup](https://user-images.githubusercontent.com/21986859/35024318-d426e93e-fb0c-11e7-8e15-41f8bb0b7db9.png)

**It's important to note to always reset these pins back to the input mode to avoid
frying them.**