def find_second_largest_num(numbers):
    if len(numbers[20:201]) < 2:
        return None
    return sorted(set(numbers[20:201]))[-2]