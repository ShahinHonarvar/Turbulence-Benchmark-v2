def find_second_largest_num(list_of_nums):
    sorted_nums = sorted(list_of_nums, reverse=True)
    if len(sorted_nums) >= 7:
        return sorted_nums[5]
    else:
        return None