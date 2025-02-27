def find_second_largest_num(numbers):
    sliced_list = numbers[31:36]
    unique_numbers = set(sliced_list)
    if len(unique_numbers) < 2:
        return None
    sorted_numbers = sorted(unique_numbers, reverse=True)
    return sorted_numbers[1]