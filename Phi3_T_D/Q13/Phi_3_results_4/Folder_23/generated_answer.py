def find_second_largest_num(numbers):
    if len(numbers[52:72]) < 2:
        return None
    subset = numbers[52:72]
    subset.sort()
    return subset[-2]