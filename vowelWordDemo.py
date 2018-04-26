#IanNolon
#4/26/28
#vowelWordDemo.py- treat strings as lists

words = input('Type in a list of words: ').split(' ')
for w in words:
    if w[0] in 'AEIOUaeiou': #if it starts with a 🅱owel
        print(w)
