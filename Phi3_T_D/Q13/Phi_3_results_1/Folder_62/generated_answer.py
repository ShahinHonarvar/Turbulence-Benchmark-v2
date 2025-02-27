def find_second_largest_num(numbers):
    sliced = numbers[90:100]
    if len(sliced) < 2:
        return None
    first, second = sorted(sliced)[-2:]
    return second