#IanNolon
#5/1/18
#gnomeSort.py - also known as stupid sort

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def mySort(A):
    '''
    procedure optimizedGnomeSort(a[]):
    for pos in 1 to length(a):
        gnomeSort(a, pos)

procedure gnomeSort(a[], upperBound):
    pos := upperBound
    while pos > 0 and a[pos-1] > a[pos]:
        swap a[pos-1] and a[pos]
        pos := pos - 1
    '''
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
