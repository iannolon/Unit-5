#IanNolon
#4/23/18
#fwordDemo.py - print out only the words that have an f

words = input('Type in some words: ').split(' ') #every time it sees a space, it will split it into different words.

for item in words:
    if 'f' in item or 'F' in item:
        print (item) #this for loop prints out the whole loop

