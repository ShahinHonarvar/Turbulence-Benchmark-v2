def find_second_largest_num(numbers):
    sliced_numbers = numbers[25:88]
    sorted_slice = sorted(sliced_numbers, reverse=True)
    return sorted_slice[1] if len(sorted_slice) > 1 else None