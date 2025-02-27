def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 26 and i <= 74 and (num % 80 == 0)]