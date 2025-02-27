def find_second_largest_num(nums):
    if len(nums[55:99]) < 2:
        return None
    sorted_nums = sorted(nums[55:99], reverse=True)
    return sorted_nums[1]