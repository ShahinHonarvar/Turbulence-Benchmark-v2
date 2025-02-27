def find_second_largest_num(numbers):
    if len(numbers) < 87:
        return None
    subset = numbers[82:87]
    subset.remove(max(subset))
    return max(subset) if subset else None