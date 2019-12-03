import math

def process_intcode_program(program):
  i = 0
  opcode = 0

  while(i < len(program) and opcode != 99):
    opcode = int(program[i])
  
    if opcode == 99:
      break
    
    val1index = program[i+1]
    val2index = program[i+2]
    storeindex = program[i+3]

    if opcode == 1:
      program[storeindex] = program[val1index] + program[val2index]
    elif opcode ==2:
      program[storeindex] = program[val1index] * program[val2index]
    else:
      raise
    
    i += 4

  
  return program[0]
