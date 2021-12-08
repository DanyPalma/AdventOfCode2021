import numpy as np 
count=0
a=0
b=0
c=0
d=0
e=0
bruh = list()
with open('./d1p2/input.txt') as input:
    np.array = input.read().splitlines() 
    for i, val in enumerate(np.array):
        if (i<1998):
          a = int(np.array[i])
          b = int(np.array[i+1])
          c = int(np.array[i+2])

          setA = a+b+c
          bruh.append(int(setA))

    array = bruh

    for i, val in enumerate(array):
      d = int(array[i])
      e = int(array[i+1])

      if (i<1997):
        if(d<e):
          count +=1
          print(count)


