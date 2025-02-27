def find_second_largest_num(nums):
    if len(nums) < 5 or len(set(nums[0:5])) < 2:
        return None
    return sorted(nums[0:5])[-2]