def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 68:
        return sorted_numbers[67]
    else:
        return None