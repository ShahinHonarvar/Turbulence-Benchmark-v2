def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 40 and i <= 400 and (num % 7 == 0)]