def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 12 and i <= 77 and (num % -19 == 0)]