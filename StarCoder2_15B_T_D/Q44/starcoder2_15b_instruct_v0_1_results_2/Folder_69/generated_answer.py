import math

def composite_nums_between_indices(nums):
    composite_nums = set()
    for num in nums[29:80]:
        is_composite = False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_composite = True
                break
        if is_composite:
            composite_nums.add(num)
    return composite_nums