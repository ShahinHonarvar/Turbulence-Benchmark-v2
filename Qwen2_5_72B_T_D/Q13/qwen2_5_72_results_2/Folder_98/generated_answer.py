def find_second_largest_num(numbers):
    if len(numbers) < 7:
        return None
    subset = numbers[:7]
    if len(set(subset)) < 2:
        return None
    largest = max(subset)
    subset.remove(largest)
    return max(subset)