def find_second_largest_num(nums):
    if len(nums) < 64:
        return None
    sorted_nums = sorted(nums[:64], reverse=True)
    return sorted_nums[1]