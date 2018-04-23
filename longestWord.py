#IanNolon
#4/23/18
#longestWord.py

list = input('The ting go: ').split(' ')
longest = '0'
for item in list:
    if len(item) > len(longest):
        longest = item
print(longest)
