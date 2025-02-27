def sum_ints_div_by_either_nums(int_list):
    sum_divisible_by_ten_or_thousand = sum((v for i, v in enumerate(int_list[80:201], start=80) if v % 10 == 0 or v % 1000 == 0))
    return sum_divisible_by_ten_or_thousand