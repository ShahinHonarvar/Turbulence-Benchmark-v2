def find_second_largest_num(numbers):
    numbers = sorted(numbers)
    if len(numbers[75:89]) >= 2:
        return numbers[75:89][-2]
    else:
        return None