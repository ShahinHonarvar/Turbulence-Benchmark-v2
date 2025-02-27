def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    subset = numbers[43:87]
    if len(set(subset)) < 2:
        return None
    return sorted(set(subset), reverse=True)[1]