def find_second_largest_num(numbers):
    """Find the second largest element from index 55 to index 98, both inclusive."""
    if len(numbers) < 99:
        return None
    sorted_numbers = sorted(numbers[55:100], reverse=True)
    return sorted_numbers[1]