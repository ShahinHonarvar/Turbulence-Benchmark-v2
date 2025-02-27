def find_second_largest_num(numbers):
    if len(numbers) < 8:
        return None
    sublist = numbers[1:9]
    if len(set(sublist)) < 2:
        return None
    return sorted(sublist, reverse=True)[1]