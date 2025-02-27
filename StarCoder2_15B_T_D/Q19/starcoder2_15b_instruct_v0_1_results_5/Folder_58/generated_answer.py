def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 266 and i < 586 and (num % 840 != 0)]