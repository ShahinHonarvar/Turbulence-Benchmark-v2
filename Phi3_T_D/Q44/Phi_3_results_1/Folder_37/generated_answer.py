from math import sqrt

def composite_nums_between_indices(nums):
    composites = set()
    for i in range(6):
        if nums[i] > 1:
            for j in range(2, int(sqrt(nums[i])) + 1):
                if nums[i] % j == 0:
                    composites.add(nums[i])
                    break
    return composites