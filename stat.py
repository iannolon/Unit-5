#IanNolon
#4/26/28
#stat.py

print('Type a list of numbers')
print('Enter \'q\' when finished')
a = 0
total = 0
nums = []
while a == 0:
    num = input('>')
    if num == 'q':
        a = 1
    else:
        total += int(num)
        nums.append(int(num))
print('Min:',min(nums))
print('Mean:',total/len(nums))
print('Max:',max(nums))
l = 0
for item in nums:
    n = list.count(item)
    if n > l:
        l += n
        m = (item)
#print('Mode:',list.count('
print([nums])
