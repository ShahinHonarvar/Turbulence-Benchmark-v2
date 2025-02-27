def all_ints_not_div_by_num(nums):
    return [num for i, num in enumerate(nums) if i not in range(10) and num % 10 != 0]