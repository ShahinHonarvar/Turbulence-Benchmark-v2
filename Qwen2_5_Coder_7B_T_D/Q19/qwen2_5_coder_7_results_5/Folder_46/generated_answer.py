def all_ints_not_div_by_num(nums):
    return [num for idx, num in enumerate(nums) if idx > 18 and idx < 60 and (num % 86 != 0)]