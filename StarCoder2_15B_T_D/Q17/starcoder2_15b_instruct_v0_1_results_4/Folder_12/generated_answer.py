def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if i >= 35 and i <= 64 and (divmod(num, -30)[1] == 0) and (divmod(num, -95)[1] == 0)]