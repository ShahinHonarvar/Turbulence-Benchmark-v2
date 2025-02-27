def find_second_largest_num(numbers):
    """Find the second largest element from index 667 to index 774, both inclusive."""
    sorted_numbers = sorted(numbers[667:775], reverse=True)
    if len(sorted_numbers) >= 2:
        return sorted_numbers[1]
    else:
        return None