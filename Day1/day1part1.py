

count=0
with open('input.txt') as input:
    array = input.read().splitlines() 
    # print(array)
    for i, val in enumerate(array):
        if(i<2000):
            if(array[i-1]<array[i]):
              count+=1


              
              
            
count = count + 1

print(count)
