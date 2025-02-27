def all_ints_div_by_num(int_list):
    try:
        return [num for num in int_list[62:64] if num % 99 == 0]
    except IndexError:
        return []