import solutionfunctions

print("Test 1")
result = solutionfunctions.calculate_required_fuel(14)
print(result)
assert result == 2

print("Test 2")
result = solutionfunctions.calculate_required_fuel(1969) 
print(result)
assert result == 966

print("Test 3")
result = solutionfunctions.calculate_required_fuel(100756)
print(result)
assert result == 50346
