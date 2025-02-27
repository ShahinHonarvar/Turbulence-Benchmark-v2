def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    filtered_numbers = numbers[62:93]
    if len(filtered_numbers) < 2:
        return None
    min_num = min(filtered_numbers)
    filtered_numbers.remove(min_num)
    return min(filtered_numbers)