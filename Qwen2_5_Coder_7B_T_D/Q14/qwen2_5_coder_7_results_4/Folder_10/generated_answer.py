def find_second_smallest_num(numbers):
    selected_numbers = numbers[62:93]
    if len(selected_numbers) < 2:
        return None
    sorted_numbers = sorted(set(selected_numbers))
    return sorted_numbers[1]