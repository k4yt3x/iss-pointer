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
~~~~
TODO
~~~~

## GPIO Header
![pi3_gpio](https://user-images.githubusercontent.com/21986859/34141154-78ec6628-e44d-11e7-8ef6-7ffcb87f79a1.png)

Pin # | Name | Name 	   | Pin #
------|------|-------------|------
 1    |      | Servo V+    | 2
 3    |      |      	   | 4
 5    |      | Servo GND  | 6
 7    |      |       	   | 8
 9    | Stepper Ground  |             | 10
 11   | Step  | Dir  | 12
 13   | MS1  | GND  	   | 14
 15   | MS2  | Servo Ctrl | 16
 17   |      |             | 18
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