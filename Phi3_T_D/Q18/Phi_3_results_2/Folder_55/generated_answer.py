def sum_ints_div_by_either_nums(int_list):
    five_digit_slice = int_list[:10]
    return sum((num for num in five_digit_slice if num % 10 == 0 or num % 100 == 0))