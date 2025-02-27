def find_second_smallest_num(numbers):
    if len(numbers) < 87:
        return None
    sliced_numbers = numbers[82:87]
    if len(sliced_numbers) < 2:
        return None
    unique_numbers = list(set(sliced_numbers))
    unique_numbers.sort()
    return unique_numbers[1] if len(unique_numbers) > 1 else None