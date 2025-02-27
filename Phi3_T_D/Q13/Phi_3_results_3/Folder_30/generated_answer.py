def find_second_largest_num(numbers):
    index_range = numbers[55:99]
    if len(index_range) < 2:
        return None
    sorted_numbers = sorted(index_range, reverse=True)
    return sorted_numbers[1]