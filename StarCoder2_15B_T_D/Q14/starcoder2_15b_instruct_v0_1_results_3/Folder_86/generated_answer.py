def find_second_smallest_num(numbers):
    selected_numbers = numbers[33:37]
    selected_numbers.sort()
    if len(selected_numbers) < 2:
        return None
    return selected_numbers[1]