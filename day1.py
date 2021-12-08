

count=0
linecount=0
with open('input.txt') as input:
    array = input.read().splitlines() 
    # print(array)
    for i, val in enumerate(array):
        if(0<i<2000):
            if(array[i-1]<array[i]):
              #print(array[i-1] + " increased to " + array[i])
             # print('increased')
              count+=1
             #  total=len(array)
           # elif(array[i-1]>array[i]):
             # print('decreased')

              
              
            
count = count + 1

print(count)
# print(total) 


# !!!!! Why was my total i beneath the actual a