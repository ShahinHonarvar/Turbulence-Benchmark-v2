def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 1 and i <= 8 and (num % 6 == 0)]