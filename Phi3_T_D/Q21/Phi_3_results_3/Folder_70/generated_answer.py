def all_ints_div_by_num(nums):
    if len(nums) > 71:
        return [num for num in nums[70:71] if num % 85 == 0]
    return []