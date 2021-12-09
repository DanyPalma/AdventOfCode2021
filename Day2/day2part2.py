aim = 0 
x = 0  # horizontal
y = 0  # depth 

with open('.\Day2\input.txt') as input: 
  for line in input.read().splitlines():

    # command, quantity 

    # if a (command) == direction, corresponding coordinate +/- b (quantity)
    a,b = line.split() 
    if a[0] == 'f':
      x += int(b)
      y += aim * int(b) 
    elif a[0] == 'u':
    #  y -= int(b)
      aim -= int(b)
    elif a[0] == 'd':
    #  y += int(b)
      aim += int(b)
    

print (x * y)




    
