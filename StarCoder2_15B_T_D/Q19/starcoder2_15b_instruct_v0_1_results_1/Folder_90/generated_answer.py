def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 767 and i < 905 and (num % -430 != 0)]