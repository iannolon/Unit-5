#IanNolon  
#4/25/18
#dictionaryDemo.py

words = ['computer','mortify','dog','firetruck','yes','python','cat']

words.sort() #alphabetical order

num = int(input('What number word do you want? '))
if num<=0 or num>=len(words)+1:
    print('Invalid number')
else:
    print(words[num-1])
