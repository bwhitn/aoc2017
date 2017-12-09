__author__ = 'brianwhitney'

nums = []
sum = 0
with open("day1.txt") as numfile:
    num = numfile.read(1)
    while num != '\n':
        nums.append(int(num))
        num = numfile.read(1)

for i in range(0, len(nums)):
    if nums[i] == nums[i-(len(nums)/2)]: #i -1 vs this for the diff
        sum += nums[i]
print str(sum)