Example programs in this folder show the sample codes/scripts that work for small specific tasks. 

A small summary of each of the programs in this folder and what they do :

1. blank_window.py: 
	This program is the hello world of pygame. It just initialized pygame and opens up a blank window on the screen

2. keyboard_input.py
	This program opens a pygame window with two blits - the ball and the goal post. The goal post is fixed. This program uses the event management in pygame to check if there are any inputs from keyboard. Using the up and down arrows, one can move the ball upwards or downwards.

3. move_ball_numbers.py
	This program opens a pygame window with a goal post, ball and the field markings. This program displays a ball that can move between 0-100% of the designated screen space to reach the goal. In order to run this, place the images in the "images' folder in the root directory. Use the numbers on the keyboard to move the ball. 
0	- 0% of the max power
100	- 100% of the max power 

4. tkinter_pygame.py
	This program opens a pygame embedded inside of a tkinter module.
 
5. read_from_text.py
	This program reads torque values from the test_array.txt file in the same folder. It converts this into an array and performs the football movement on the field as per the torque values
