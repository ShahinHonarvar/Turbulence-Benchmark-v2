def find_second_largest_num(numbers):
    subset = numbers[40:201]
    if len(subset) < 2:
        return None
    subset.sort()
    second_largest = subset[-2]
    return second_largest