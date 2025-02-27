def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 9:
        return None
    sorted_numbers = sorted(numbers[:9], reverse=True)
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None