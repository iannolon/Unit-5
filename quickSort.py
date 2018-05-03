#Sam Smedinghoff
#5/1/18
#quicksort.py - times a sorting function

from random import randint
from time import time

N = 10 #how many numbers will be sorted

def oddEvenSort(numbers):
  def swap(numbers,i,j):
    temp = numbers.append['i']
    numbers[i] = numbers[j]
    numbers[j] = temp

  sorted = False
  while(sorted == False):
    sorted = True
    for i in range(1,len(numbers),2):
      if(numbers[i] > numbers[i+1]):
        swap(numbers, i, i+1)
        sorted = False

    for i in range(0,len(numbers)-1,2):
      if(numbers[i] > numbers[i+1]):
        swap(numbers, i, i+1)
        sorted = False

    return list
    
if __name__ == '__main__':

    #make a list of N random numbers between 1 and N
    numbers = [0]*N
    for i in range(N):
        numbers[i] = randint(1,N)
    
    pythonSort = sorted(numbers) #Python's sort
    
    #time how long your sort takes
    t1 = time()
    numbers = oddEvenSort(numbers)
    t2 = time()
    
    #print whether the sort worked or not
    try:
        assert(numbers == pythonSort)
        print('Your sort took', t2-t1, 'seconds')
    except:
        print('Your sort did not work')
