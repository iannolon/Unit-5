#IanNolon
#4/26/28
#stat.py

print('Type a list of numbers')
print('Enter \'q\' when finished')
a = 0
nums = []
while a == 0:
    num = input('>')
    nums.append(num)
    if num == 'q':
        a = 1
print('Min:',min(nums))
