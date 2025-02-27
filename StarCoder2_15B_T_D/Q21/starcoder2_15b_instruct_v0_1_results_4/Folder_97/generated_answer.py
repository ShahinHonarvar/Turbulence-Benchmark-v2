def all_ints_div_by_num(nums):
    return [num for idx, num in enumerate(nums) if idx >= 17 and idx <= 63 and (num % 89 == 0)]