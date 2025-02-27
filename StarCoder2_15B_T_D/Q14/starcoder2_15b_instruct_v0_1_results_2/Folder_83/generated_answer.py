def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    if len(sorted_numbers) >= 201:
        return sorted_numbers[90:201][1]
    else:
        return None