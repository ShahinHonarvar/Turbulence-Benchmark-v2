def find_second_largest_num(nums):
    slicing = nums[56:67]
    if len(slicing) < 2:
        return None
    largest = max(slicing)
    return max((x for x in slicing if x != largest))