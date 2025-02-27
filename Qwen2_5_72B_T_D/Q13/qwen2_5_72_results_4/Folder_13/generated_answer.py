def find_second_largest_num(nums):
    if len(nums) < 88 or len(set(nums[25:88])) < 2:
        return None
    unique_nums = set(nums[25:88])
    unique_nums.remove(max(unique_nums))
    return max(unique_nums)