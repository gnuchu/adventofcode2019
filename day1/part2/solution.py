import solutionfunctions
import sys
sys.path.append('../../functions')
import helperfunctions

data = helperfunctions.read_input()
total = 0

for mass in data:
  total += solutionfunctions.calculate_required_fuel(mass)

helperfunctions.write_output(str(total))
print(str(total))
