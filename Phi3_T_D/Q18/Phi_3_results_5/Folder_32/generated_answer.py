def sum_ints_div_by_either_nums(nums_list):
    sum_divisible = sum((nums_list[idx] for idx in range(25, 96) if nums_list[idx] % 51 == 0 or nums_list[idx] % 77 == 0))
    return sum_divisible