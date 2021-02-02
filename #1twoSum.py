
def twoSum(nums, target):
    h = {}
    for index, num in enumerate(nums):
        n = target - num
        if n in h:
            return [h[n], index]

        h[num] = index


print(twoSum([3, 2, 5, 3], 6))
