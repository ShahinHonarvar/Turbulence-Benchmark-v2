def find_second_largest_num(numbers):
    try:
        sorted_numbers = sorted(numbers, reverse=True)
        return sorted_numbers[1]
    except IndexError:
        return None