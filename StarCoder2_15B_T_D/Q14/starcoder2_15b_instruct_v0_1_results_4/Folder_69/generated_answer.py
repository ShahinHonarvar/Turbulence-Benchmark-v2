def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 88:
        return sorted_numbers[25:88][1]
    else:
        return None