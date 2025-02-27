def find_second_smallest_num(numbers):
    if len(numbers) < 5 or min(numbers[1:6]) is None:
        return None
    second_smallest = sorted(set(numbers[1:6]))[1]
    return second_smallest