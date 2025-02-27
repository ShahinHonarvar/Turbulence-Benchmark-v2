def find_second_largest_num(nums):
    if len(nums[55:99]) < 2:
        return None
    max_val = max(nums[55:99])
    nums[55:99] = [x for x in nums[55:99] if x != max_val]
    return max(nums[55:99])