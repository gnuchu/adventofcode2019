import solutionfunctions
import sys
sys.path.append('../../functions')
import helperfunctions

data_str = helperfunctions.read_input()[0].split(",")
data = list(map(lambda x: int(x), data_str))
#Fix the program
data[1] = 12
data[2] = 2
#

result = solutionfunctions.process_intcode_program(data)
helperfunctions.write_output(str(result))
print(result)




