def find_second_smallest_num(numbers):
    numbers = sorted(numbers)
    if len(numbers) >= 609:
        return numbers[608]
    else:
        return None