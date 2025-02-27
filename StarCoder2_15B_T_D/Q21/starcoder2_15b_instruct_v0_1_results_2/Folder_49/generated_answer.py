def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 30 and i <= 300 and (num % 5 == 0)]