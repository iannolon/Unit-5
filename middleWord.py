#IanNolon
#4/23/18
#middleWord.py

list = input('the ting go: ').split(' ')
mid = len(list)/2
if len(list)%2 == 0:
    otherMid = mid - 1
    print(list[otherMid])
print(list[mid])
