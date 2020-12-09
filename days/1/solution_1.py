with open('nums.txt', 'r') as f:
    nums = [int(line) for line in f]

print(nums)
target = 2020


def two_sum(nums, target):
    for idx, i in enumerate(nums):
        if (target - i) in nums:
            return i * (target - i)

def three_sum(nums, target):
    head = 0

    nums.sort()


    for idx, i in enumerate(nums):
        pass
