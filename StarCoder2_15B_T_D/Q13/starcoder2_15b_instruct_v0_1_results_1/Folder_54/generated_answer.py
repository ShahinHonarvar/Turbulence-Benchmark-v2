def find_second_largest_num(nums):
    sublist = nums[34:56]
    max1, max2 = (float('-inf'), float('-inf'))
    for num in sublist:
        if num > max1:
            max1, max2 = (num, max1)
        elif num > max2:
            max2 = num
    if max2 == float('-inf'):
        return None
    return max2