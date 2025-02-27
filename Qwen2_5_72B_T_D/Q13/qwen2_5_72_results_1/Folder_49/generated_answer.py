def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) < 81:
        return None
    subset = numbers[80:201]
    if len(set(subset)) < 2:
        return None
    subset.sort(reverse=True)
    return subset[1]