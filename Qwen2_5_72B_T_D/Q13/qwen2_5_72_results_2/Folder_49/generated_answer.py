def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) > 201:
        return None
    subset = numbers[80:201]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset)
    return second_largest