import math

def calculate_required_fuel(mass):
  total = 0
  m = fuelrequired(mass)

  while(m > 0):
    total += m
    m = fuelrequired(m)

  return total

def fuelrequired(m):
  return math.floor(int(m)/3)-2
