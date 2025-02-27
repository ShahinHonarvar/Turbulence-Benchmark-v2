def all_odd_ints_exclusive(int_list):
    if not isinstance(int_list, list) or not all((isinstance(i, int) for i in int_list)):
        raise TypeError('The argument must be a list of integers.')
    if len(int_list) < 573:
        raise IndexError('The list must have at least 573 elements.')
    return [i for i in int_list[295:573] if i % 2 != 0]