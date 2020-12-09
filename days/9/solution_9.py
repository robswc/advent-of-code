"""
Solution for: https://adventofcode.com/2020/day/9
Notes: Utilizes sliding windows.
"""


with open('nums.txt', 'r') as f:
    nums = [int(line) for line in f]

def encode_error(nums, length):
    # Set pointers to be length:num's length
    for idx in range(length, len(nums)):
        # Create a list to act as a pool of available numbers
        pool = nums[idx-length:idx]
        # Set a continue lock, for ever new num we iterate.
        locked = True
        # For loop, in range length
        for x in range(length):
            # For loop, in range length, again. (headers)
            for y in range(length):
                # If loop1 + loop2 == nums index of original loop
                if pool[x] + pool[y] == nums[idx]:
                    # Set locked to false (which will continue)
                    locked = False

        # Once the loop is no longer locked, the number at idx is returned.
        if locked:
            return nums[idx]


def encode_error_2(nums, target):
    # Create loop to track index
    for idx in range(len(nums)):
        # Create second loop, tracking index of second pointer.
        for x in range(idx+1, len(nums)):
            # Create continous set list
            c_set = nums[idx:x]
            # Check if sum of set is our target
            if sum(c_set) == target:
                return min(c_set) + max(c_set)


part1 = encode_error(nums, 25)
print(part1)
part2 = encode_error_2(nums, part1)
print(part2)