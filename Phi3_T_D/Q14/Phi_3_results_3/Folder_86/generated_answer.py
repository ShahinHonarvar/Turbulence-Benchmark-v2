def find_second_smallest_num(numbers):
    try:
        return sorted(numbers[33:36])[1]
    except IndexError:
        return None