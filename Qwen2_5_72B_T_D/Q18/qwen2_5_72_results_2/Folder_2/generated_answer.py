def sum_ints_div_by_either_nums(nums):
    return sum((num for num in nums[73:87] if num % 54 == 0 or num % 82 == 0)) if 73 < len(nums) else 0