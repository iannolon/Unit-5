#IanNolon
#5/7/18
#quiz5.py

def penultimate(list):
    length = len(list)
    return list[length-2]
def plusEquals(numList,num):
    for number in numList:
        numList[number-1] = number+num
    return numList
def smallest(k):
    small = 100000
    for item in k:
        if item < small:
            small = item
    return small
    
print(penultimate([3,4,5,6,7]))
print(plusEquals([1,2,3,4],10))
print(smallest([1,2,3,4]))
