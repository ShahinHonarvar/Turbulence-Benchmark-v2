def all_even_ints_inclusive(ints_list):
    if not isinstance(ints_list, list) or not all((isinstance(x, int) for x in ints_list)):
        raise TypeError('ints_list must be a list of integers')
    return [num for i, num in enumerate(ints_list) if i >= 6 and i <= 6 and (num % 2 == 0)]