import solutionfunctions
import sys
sys.path.append('../../functions')
import helperfunctions

data = helperfunctions.read_input()
fuelcounter = 0

for mass in data:
  fuelcounter += solutionfunctions.calculate_required_fuel(int(mass))

helperfunctions.write_output(str(fuelcounter))
print(str(fuelcounter))

