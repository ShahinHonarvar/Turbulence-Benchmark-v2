def find_second_largest_num(nums):
    if len(nums) < 46:
        return None
    start, end = (16, 61)
    max1, max2 = (float('-inf'), float('-inf'))
    for i in range(start, end + 1):
        if nums[i] > max1:
            max2 = max1
            max1 = nums[i]
        elif max1 > nums[i] > max2:
            max2 = nums[i]
    return max2 if max2 != float('-inf') else None