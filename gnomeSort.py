#IanNolon
#5/1/18
#gnomeSort.py - also known as stupid sort
'''
Gnome Sort is based on the technique used by the standard Dutch Garden Gnome.
Here is how a garden gnome sorts a line of flower pots. 
Basically, he looks at the flower pot next to him and the previous one; 
if they are in the right order he steps one pot forward, 
otherwise he swaps them and steps one pot backwards. 
Boundary conditions: if there is no previous pot, he steps forwards; 
if there is no pot next to him, he is done.
'''

from random import randint
from time import time

N = 1000 #how many numbers will be sorted

def mySort(A):
    pos = 0
    temp = 0
    while pos < len(numbers):
        if (pos == 0 or numbers[pos] >= numbers[pos-1]):
            pos += 1
        else:
            numbers[pos],numbers[pos-1] = numbers[pos-1],numbers[pos]
            pos -= 1
    return A
    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = mySort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
