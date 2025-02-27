def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    second_smallest = sorted_numbers[19]
    if len(sorted_numbers) >= 200:
        return sorted_numbers[200]
    else:
        return None