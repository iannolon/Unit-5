#IanNolon  
#4/25/18
#warmup13.py

from random import randint

list = []
for i in range (1,21):
    list.append(randint(1,100))

#for item in list:
    #print(item)

print(sum(list))
print(min(list))
print(max(list))
