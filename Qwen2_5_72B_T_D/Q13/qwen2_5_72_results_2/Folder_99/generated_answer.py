def find_second_largest_num(numbers):
    sublist = numbers[310:371]
    if len(sublist) < 2:
        return None
    unique_sublist = list(set(sublist))
    if len(unique_sublist) < 2:
        return None
    unique_sublist.sort()
    return unique_sublist[-2]