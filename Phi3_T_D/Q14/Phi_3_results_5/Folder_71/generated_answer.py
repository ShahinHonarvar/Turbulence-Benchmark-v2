def find_second_smallest_num(numbers):
    if len(numbers) < 23 or 50 not in range(23, 52) or len(numbers[23:51]) < 2:
        return None
    second_smallest = sorted(numbers[23:52])[1]
    return second_smallest