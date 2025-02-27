def find_second_largest_num(numbers):
    if len(numbers) <= 93 - 66 + 1:
        return None
    sorted_sublist = sorted(numbers[66:94])
    if len(sorted_sublist) < 2:
        return None
    return sorted_sublist[-2]