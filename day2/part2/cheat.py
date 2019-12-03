for x in range(100):
  for y in range(100):
    #extract the code from the file and load it into an array for processing
    input = open("input/input.txt", "r")
    code = input.read()
    input.close()
    code = code.split(",")

    #the array elements are currently strings; turn them into integers
    for i in range(len(code)):
      code[i] = int(code[i])

    #set the initial inputs
    code[1] = x
    code[2] = y

    #run the intcode
    for i in range(0, len(code)-1, 4):
      one = code[i]
      two = code[i+1]
      three = code[i+2]
      four = code[i+3]
      if (one == 1):
          code[four] = code[two] + code[three]
      elif (one == 2):
          code[four] = code[two] * code[three]
      elif (one == 99):
          break

    #check if the output matches the desired answer and print the result to the console.
    if(code[0] == 19690720):
      print("The inputs needed to obtain the output of 19690720 are " +
            str(x) + " and " + str(y))
