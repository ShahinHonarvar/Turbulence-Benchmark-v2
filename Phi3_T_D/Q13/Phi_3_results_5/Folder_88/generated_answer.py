def find_second_largest_num(nums):
    if len(nums[4:9]) < 2:
        return None
    sliced_nums = sorted(nums[4:9], reverse=True)
    return sliced_nums[1]