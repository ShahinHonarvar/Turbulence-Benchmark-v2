def find_second_smallest_num(nums):
    if len(nums) < 67 or len(nums) > 67:
        return None
    return sorted(nums[64:67])[1]