def read_input(path="input/input.txt"):
  with open(path, 'r') as stream:
    data = stream.read()
  
  data_array = data.split("\n")
  return data_array

def write_output(data, path="output/solution.txt"):
  with open(path, "w") as file:
    file.write(data)
