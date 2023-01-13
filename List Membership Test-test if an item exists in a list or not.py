setA = {1, 2, 3, 4, 5}
setB = {1, 2, 5}

print("setA: ", setA)
print("setB: ", setB)

subSet = True

for i in setB:
  if i not in setA:
    subSet = False

if subSet == False:
  print("SetB is not a subset of SetA")
else:
  print("SetB is a subset of SetA")

for i in setA:
  if i not in setB:
    subSet = False

if subSet == False:
  print("SetA is not a subset of SetB")
else:
  print("SetA is a subset of SetB")
