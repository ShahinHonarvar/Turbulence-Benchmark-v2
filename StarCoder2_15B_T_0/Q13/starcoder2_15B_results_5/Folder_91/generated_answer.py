def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    sorted_nums = sorted(nums[:6], reverse=True)
    return sorted_nums[1]