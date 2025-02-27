import math

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(0, 3):
        num = nums[i]
        for j in range(2, int(math.sqrt(num)) + 1):
            if num % j == 0:
                composite_nums.add(num)
                break
    return composite_nums