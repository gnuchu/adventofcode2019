import solutionfunctions
import sys
sys.path.append('../../functions')
import helperfunctions

class BreakOut(Exception): pass

def load_memory():
  data_str = helperfunctions.read_input()[0].split(",")
  program = list(map(lambda x: int(x), data_str))
  return program

memory = load_memory()

noun = 0
verb = 0

try:
  for i in range(100):
    for j in range(100):
      memory[1] = i
      memory[2] = j

      result = solutionfunctions.process_intcode_program(memory)
      if int(result) == 19690720:
        noun = i
        verb = j
        raise BreakOut
      
      memory = []
      memory = load_memory()
    j+=1
  i+=1
except BreakOut:
  result = 100 * int(noun) + int(verb)
  message = f"Noun is {noun}, Verb is {verb}. Result is: {result}"
  helperfunctions.write_output(message)
  print(message)
except:
  print("Other error")
  print(memory)
