def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 5 and i <= 6 and (num % -6 == 0)]