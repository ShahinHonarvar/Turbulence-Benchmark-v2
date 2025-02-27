def find_second_largest_num(nums):
    if len(nums) < 19 or len(nums[30:49]) < 2:
        return None
    return sorted(nums[30:49], reverse=True)[1]