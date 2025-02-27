def find_second_largest_num(numbers):
    filtered_numbers = numbers[35:50]
    if len(filtered_numbers) < 2:
        return None
    max_num = max(filtered_numbers)
    filtered_numbers.remove(max_num)
    second_max = max(filtered_numbers) if filtered_numbers else None
    return second_max