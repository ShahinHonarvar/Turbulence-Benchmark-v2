def all_ints_div_by_both_two_nums(nums):
    return [num for i, num in enumerate(nums) if 154 <= i <= 798 and divmod(num, 275)[1] == 0 and (divmod(num, 580)[1] == 0)]