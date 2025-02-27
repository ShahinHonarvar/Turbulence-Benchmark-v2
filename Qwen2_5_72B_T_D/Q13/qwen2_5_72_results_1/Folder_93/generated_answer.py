def find_second_largest_num(numbers):
    if len(numbers) < 95:
        return None
    sublist = numbers[75:95]
    if len(set(sublist)) < 2:
        return None
    return sorted(set(sublist), reverse=True)[1]