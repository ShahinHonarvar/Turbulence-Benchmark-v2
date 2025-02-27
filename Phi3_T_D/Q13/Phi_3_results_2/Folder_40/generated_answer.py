def find_second_largest_num(numbers):
    lst = sorted(numbers[:3])
    return lst[-2] if len(lst) >= 2 else None