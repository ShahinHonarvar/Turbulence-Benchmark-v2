def find_second_smallest_num(numbers):
    subset = numbers[62:64]
    if len(subset) != 2:
        return None
    return sorted(subset)[1]