def sum_ints_div_by_either_nums(lst):
    relevant_numbers = lst[0:2]
    return sum((num for num in relevant_numbers if num % 2 == 0 or num % 1 == 0))