# Raspberry Pi ISS Pointer

Dev: djgood@github.com  
Dev: k4yt3x@github.com  
Date Created: N/A  
Last Modified: Dec 18, 2017

## Current Version: 0.1 alpha

## Change Logs:
1. Project Imported

## Description
The raspberry pi ISS Pointer is a simple device that will always point to the current location of the International Space Station (ISS).
This project is initialized as an ISU project.

## Usage
~~~~
TODO
~~~~

## GPIO Header
![Pi3 GPIO Header Image](https://github.com/djgood/isspointer/raw/master/pi3gpioheader.jpg)

Pin # | Name | Name 	   | Pin #
------|------|-------------|------
 1    |      | Servo V+    | 2
 3    |      |      	   | 4
 5    |      | 	           | 6
 7    |      |       	   | 8
 9    |      |             | 10
 11   | MS1  | Servo Ctrl  | 12
 13   | MS2  | GND  	   | 14
 15   |      | Stepper Dir | 16
 17   |      | Stepper Step | 18
 19   |      | 		   | 20
 21   |      |             | 22
 23   |      |             | 24
 25   |      |             | 26
 27   |      |             | 28
 29   |      |             | 30
 31   |      |             | 32
 33   |      |             | 34
 35   |      |             | 36
 37   |      |             | 38
 39   |      |             | 40

**It's important to note to always reset these pins back to the input mode to avoid
frying them.**