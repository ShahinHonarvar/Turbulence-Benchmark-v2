def sum_ints_div_by_either_nums(lst):
    if not isinstance(lst, list) or not all((isinstance(x, int) for x in lst)):
        raise TypeError('lst must be a list of integers')
    sum_int = 0
    for i, num in enumerate(lst):
        if i >= 36 and i <= 85 and (num % -27 == 0) or num % -96 == 0:
            sum_int += num
    return sum_int