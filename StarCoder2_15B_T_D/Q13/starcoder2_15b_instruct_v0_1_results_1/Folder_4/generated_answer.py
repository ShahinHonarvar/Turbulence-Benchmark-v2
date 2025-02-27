def find_second_largest_num(nums):
    sublist = nums[12:93]
    max_num = max(sublist)
    second_largest_num = None
    for num in sublist:
        if num < max_num:
            if second_largest_num is None or num > second_largest_num:
                second_largest_num = num
    return second_largest_num