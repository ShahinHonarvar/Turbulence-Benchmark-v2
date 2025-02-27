def find_second_largest_num(nums):
    sorted_nums = sorted(nums[100:201], reverse=True)
    if len(sorted_nums) < 2:
        return None
    return sorted_nums[1]