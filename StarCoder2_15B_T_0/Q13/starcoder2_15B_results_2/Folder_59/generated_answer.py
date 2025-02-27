def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    sorted_nums = sorted(nums[:10], reverse=True)
    return sorted_nums[1]