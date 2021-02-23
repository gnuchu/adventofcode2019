import sys
sys.path.append('../../functions')
import helperfunctions
import solutionfunctions

raw_input = helperfunctions.read_multi_line_input('input/test.txt')
lines = raw_input.split("\n")
for line in lines:
  print(line)