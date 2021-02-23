import math 
def process_direction_instructions(moves):
  #Data is an array of movements.
  position = [0,0]
  past_postions = []
  past_postions_dict = {}

  for move in moves:
    direction = move[0]
    steps = int(move[1:])

    if direction == 'L' or direction == 'D':
      steps *= -1
    
    if direction == 'L' or direction == 'R':
      position[0] += steps

    if direction == 'U' or direction == 'D':
      position[1] += steps
    
    past_postions.append(position[:])
    if tuple(position) in past_postions_dict:
      past_postions_dict[tuple(position)] += 1
    else:
      past_postions_dict[tuple(position)] = 1
  
  past_postions.sort(key=lambda x: manhattan_distance(x))
  print(past_postions_dict)

  print(f"End postion: {position}")

def manhattan_distance(pointx, pointy=[0,0]):
  distance = (pointx[0] - pointy[0]) + (pointx[1] - pointy[1])
  return math.floor(distance)

