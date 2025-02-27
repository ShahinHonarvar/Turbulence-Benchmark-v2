def find_second_largest_num(nums):
    start, end = (26, min(52, len(nums)))
    sublist = nums[start:end + 1]
    if len(sublist) < 2:
        return None
    max1, max2 = (None, None)
    for num in sublist:
        if max1 is None or num > max1:
            max2, max1 = (max1, num)
        elif max2 is None or num > max2:
            max2 = num
    return max2