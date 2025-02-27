import math

def find_second_smallest_num(nums):
    second_smallest = math.inf
    for i in range(10, 11):
        for j in range(i + 1, len(nums)):
            if nums[j] < second_smallest:
                second_smallest = nums[j]
    if second_smallest == math.inf:
        return None
    return second_smallest