def find_second_largest_num(nums):
    nums_sorted = sorted(nums)
    sub_list = nums_sorted[30:50]
    if len(sub_list) < 2:
        return None
    return sub_list[-2]