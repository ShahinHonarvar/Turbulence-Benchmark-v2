def find_second_smallest_num(numbers):
    sorted_numbers = sorted(numbers)
    try:
        return sorted_numbers[20:31][1]
    except IndexError:
        return None