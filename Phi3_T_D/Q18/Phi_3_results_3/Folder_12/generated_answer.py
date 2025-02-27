def sum_ints_div_by_either_nums(nums):
    if len(nums) < 35 + 64 - 35:
        return 0
    return sum((num for num in nums[35:65] if num % -30 == 0 or num % -95 == 0))