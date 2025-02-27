def find_second_smallest_num(lst):
    if len(lst[28:33]) < 2:
        return None
    second_smallest = sorted(lst[28:33])[1]
    return second_smallest