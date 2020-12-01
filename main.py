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
yobgib = []

for w in range(len(l)):
  bigboy.append(ordval(l[w]))

for w in range(len(l)):
  yobgib.append(droval(l[w]))

dome = (staz.mode(bigboy))

newguy = []
fllla = []

for w in range(len(l)):
  if (bigboy[w] == yobgib[w]):
    newguy.append(l[w])
    fllla.append(bigboy[w])

print(staz.mode(fllla))

for w in range(len(newguy)):
  if ordval(newguy[w]) == 108:
    print(newguy[w])