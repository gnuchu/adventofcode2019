import sys
sys.path.append('../../functions')
import helperfunctions
import solutionfunctions

input = helperfunctions.read_input('input/test.txt')
test_data = input[0].split(',')

result = solutionfunctions.process_direction_instructions(test_data)

