import math

def composite_nums_between_indices(nums):
    composite_nums = set()
    for i in range(21, 98):
        is_composite = False
        for j in range(2, int(math.sqrt(nums[i])) + 1):
            if nums[i] % j == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(nums[i])
    return composite_nums