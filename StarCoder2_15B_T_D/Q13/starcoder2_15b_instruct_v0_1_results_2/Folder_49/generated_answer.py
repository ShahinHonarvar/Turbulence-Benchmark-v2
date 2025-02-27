def find_second_largest_num(numbers):
    sorted_numbers = sorted(numbers, reverse=True)
    try:
        return sorted_numbers[1]
    except IndexError:
        return None