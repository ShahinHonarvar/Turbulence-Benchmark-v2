def find_second_largest_num(numbers):
    sublist = numbers[62:100]
    if len(sublist) < 2:
        return None
    unique_sublist = list(set(sublist))
    unique_sublist.sort()
    if len(unique_sublist) < 2:
        return None
    return unique_sublist[-2]