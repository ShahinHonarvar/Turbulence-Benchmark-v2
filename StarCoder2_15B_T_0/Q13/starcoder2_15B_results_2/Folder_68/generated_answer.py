def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sorted_nums = sorted(nums[:9], reverse=True)
    return sorted_nums[1]