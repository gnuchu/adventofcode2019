import sys
sys.path.append('../../functions')
import helperfunctions
import solutionfunctions

pointx = [4,3]
pointy = [0,0]
distance = solutionfunctions.manhattan_distance(pointx, pointy=pointy)
assert distance == 7

pointy = [-1,-1]
pointx = [3,2]
distance = solutionfunctions.manhattan_distance(pointx, pointy=pointy)
assert distance == 7

pointy = [1,1]
pointx = [5,4]
distance = solutionfunctions.manhattan_distance(pointx, pointy=pointy)
assert distance == 7



