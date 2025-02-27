def sum_ints_div_by_either_nums(int_list):
    return sum((num for i, num in enumerate(int_list[20:201]) if num % 20 == 0 or num % 200 == 0))