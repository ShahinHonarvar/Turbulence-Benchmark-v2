def find_second_smallest_num(nums):
    a = nums[32:36]
    a.sort()
    return a[1] if len(a) > 1 else None