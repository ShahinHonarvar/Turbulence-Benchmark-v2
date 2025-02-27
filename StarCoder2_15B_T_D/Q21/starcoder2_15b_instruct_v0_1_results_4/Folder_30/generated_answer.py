def all_ints_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i >= 59 and i <= 79 and (num % -82 == 0)]