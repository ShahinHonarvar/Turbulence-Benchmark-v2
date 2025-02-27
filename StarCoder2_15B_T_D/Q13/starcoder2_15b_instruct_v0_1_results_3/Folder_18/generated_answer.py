def find_second_largest_num(nums):
    sorted_list = sorted(nums[35:50], reverse=True)
    if len(sorted_list) >= 2:
        return sorted_list[1]
    else:
        return None