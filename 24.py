from z3 import *

# Damn, I am so rusty at python
hails = []
file = open("input", 'r')
for line in file.readlines():
	(ps, vs) = line.split(' @ ')
	ps = [int(p) for p in ps.split(', ')]
	vs = [int(v) for v in vs.split(', ')]
	hails.append([ps, vs])
file.close()

# Symbolic variables for our rock
x, y, z = Ints('x y z')
dx, dy, dz = Ints('dx dy dz')

s = Solver()

for (i, hail) in enumerate(hails):
	(x1, y1, z1), (dx1, dy1, dz1) = hail
	t = Int(f't_{i}') # Must give the time variables unique names
	
	# Add constraint per piece of hail
	s.add(x + t * dx == x1 + t * dx1)
	s.add(y + t * dy == y1 + t * dy1)
	s.add(z + t * dz == z1 + t * dz1)

	# Must intersect after t = 0
	s.add(t >= 0)

# Try to solve the equation system, and check if it is solvable
if s.check() != sat:
	print("Solution not found")
	exit()

# Get the values! Apparently we get it as a symbol, so just eval it
solution = s.model()
ans = solution[x] + solution[y] + solution[z]
print(eval(str(ans))) # I miss zote and ans >> str >> eval >> print


