def all_ints_div_by_both_two_nums(numbers):
    return [n for i, n in enumerate(numbers[306:958]) if n % 982 == 0 and n % 319 == 0]