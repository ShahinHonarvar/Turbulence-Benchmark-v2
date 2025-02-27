def find_second_largest_num(lst):
    start_index, end_index = (56, 57)
    sublist = sorted(lst[start_index:end_index + 1])
    if len(sublist) >= 2:
        return sublist[-2]
    return None