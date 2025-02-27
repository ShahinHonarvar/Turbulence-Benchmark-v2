def all_ints_div_by_both_two_nums(int_list):
    if not isinstance(int_list, list) or not all((isinstance(num, int) for num in int_list)):
        raise ValueError("Invalid input: 'int_list' must be a list of integers.")
    return [num for i, num in enumerate(int_list) if i >= 0 and i <= 3 and (num % 11 == 0) and (num % -7 == 0)]