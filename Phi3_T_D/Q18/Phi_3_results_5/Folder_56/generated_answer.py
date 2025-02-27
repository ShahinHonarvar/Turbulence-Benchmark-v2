def sum_ints_div_by_either_nums(lst):
    relevant_section = lst[7:10]
    return sum((num for num in relevant_section if num % -9 == 0 or num % -7 == 0))