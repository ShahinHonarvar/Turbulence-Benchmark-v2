def find_second_smallest_num(nums):
    sliced_nums = nums[10:101]
    unique_nums = sorted(set(sliced_nums))
    if len(unique_nums) >= 2:
        return unique_nums[1]
    else:
        return None