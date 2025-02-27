def find_second_smallest_num(numbers):
    filtered_numbers = numbers[70:85]
    if len(filtered_numbers) < 2:
        return None
    second_smallest = sorted(filtered_numbers)[1]
    return second_smallest