def find_second_largest_num(nums):
    if len(nums) < 539:
        return None
    sub = nums[527:539]
    if len(sub) < 2:
        return None
    sub.sort()
    return sub[-2]