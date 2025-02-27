def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 639:
        return sorted_numbers[639]
    else:
        return None