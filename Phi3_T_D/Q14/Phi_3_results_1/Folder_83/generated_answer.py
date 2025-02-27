def find_second_smallest_num(numbers):
    if 90 <= len(numbers) <= 201:
        sliced_numbers = numbers[89:201]
        unique_numbers = set(sliced_numbers)
        if len(unique_numbers) < 2:
            return None
        return sorted(unique_numbers)[1]
    return None