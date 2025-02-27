def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    sorted_nums = sorted(nums[:7], reverse=True)
    return sorted_nums[1]