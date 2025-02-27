def find_second_largest_num(numbers):
    if len(numbers) < 80:
        return None
    subset = numbers[29:80]
    if len(set(subset)) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]