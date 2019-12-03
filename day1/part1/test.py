import localfunctions

print("Test 1")
assert localfunctions.calculate_required_fuel(12) == 2

print("Test 2")
assert localfunctions.calculate_required_fuel(14) == 2

print("Test 3")
assert localfunctions.calculate_required_fuel(1969) == 654

print("Test 4")
assert localfunctions.calculate_required_fuel(100756) == 33583
