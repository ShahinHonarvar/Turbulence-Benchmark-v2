def find_second_largest_num(numbers):
    if len(numbers) < 201 or len(numbers) > 201 or len(set(numbers[80:201])) < 2:
        return None
    subset = numbers[80:201]
    largest = max(subset)
    subset.remove(largest)
    second_largest = max(subset) if subset else None
    return second_largest