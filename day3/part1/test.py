import sys
sys.path.append('../../functions')
import helperfunctions
import solutionfunctions
from turtle import *

def get_heading(direction):
  heading = 0

  if heading == 'U':
    heading = 0
  elif direction == 'D':
    heading = 180
  elif direction == 'R': 
    heading = 90
  elif direction == 'L':
    heading = 270

  return heading

input = helperfunctions.read_multiline_input('input/input.txt')
lines = input.split('\n')
test_data = input[0].split(',')
print(lines[1])

colors = ['red', 'blue']  #Assumption here that we're just drawing 2 lines.

for i, line in enumerate(lines, start=0):
  instructions = line.split(',')
  penup()
  goto(0,0)
  pendown()
  pencolor(colors[i])

  for instruction in instructions:
    direction = instruction[0]
    steps = int(instruction[1:])/10

    setheading(get_heading(direction))
    forward(steps)
