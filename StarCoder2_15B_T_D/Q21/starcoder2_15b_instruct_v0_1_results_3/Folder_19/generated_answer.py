def all_ints_div_by_num(nums):
    return [num for idx, num in enumerate(nums) if idx >= 1 and idx <= 8 and (num % 6 == 0)]