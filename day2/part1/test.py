import solutionfunctions

print('Test 1')
data = [1, 0, 0, 0, 99]
result = solutionfunctions.process_intcode_program(data)
print(result)
assert result == 2

print('Test 2')
data = [1, 1, 1, 4, 99, 5, 6, 0, 99]
result = solutionfunctions.process_intcode_program(data)
print(result)
assert result == 30
