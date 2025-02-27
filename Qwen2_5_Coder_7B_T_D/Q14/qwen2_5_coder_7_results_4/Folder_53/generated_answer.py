def find_second_smallest_num(nums):
    return sorted(nums[1:101])[1] if len(nums[1:101]) > 1 else None