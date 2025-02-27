def find_second_smallest_num(numbers):
    start = 75
    end = 85
    if len(numbers) < end - start + 1:
        return None
    sorted_numbers = sorted(numbers[start:end + 1])
    return sorted_numbers[1] if len(sorted_numbers) > 1 else None