def find_second_smallest_num(numbers):
    start, end = (36, 46)
    selected_numbers = numbers[start:end + 1]
    if len(selected_numbers) < 2:
        return None
    sorted_numbers = sorted(selected_numbers)
    return sorted_numbers[1]