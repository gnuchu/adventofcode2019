class IntCodeComputer:

  def __init__(self, memory=[]):
    self.memory = memory
    self.opcode_pointer = 0
  
  def opcode(self):
    return self.memory[self.opcode_pointer]

  def reset_memory(self):
    self.memory = []
  
  def pointer_increment(self):
    if self.opcode == 99:
      self.opcode_pointer += 1
    else:
      self.opcode_pointer += 4
  
