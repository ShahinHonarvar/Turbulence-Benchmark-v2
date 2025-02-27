def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    sublist = numbers[68:87]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[-2]