def find_second_smallest_num(numbers):
    if len(numbers[56:83]) < 2:
        return None
    numbers[56:83] = sorted(numbers[56:83])
    return numbers[56]