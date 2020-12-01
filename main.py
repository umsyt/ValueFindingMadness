import statistics as staz

def ordval(s):
  k = 0
  for l in s:
    k += ord(l)
  k -= (len(s)*96)
  return k

def droval(s):
  k = 0
  for l in s:
    k += (123-ord(l))
  return k

with open('dict') as f:
    l = f.read().splitlines()

bigboy = []

for w in range(len(l)):
  bigboy.append(ordval(l[w]))

dome = (staz.mode(bigboy))

newguy = []

for w in range(len(l)):
  if bigboy[w] == 113:
    newguy.append(l[w])

print(newguy)