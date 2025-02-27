def find_second_smallest_num(numbers):
    return sorted(numbers[:6])[1] if len(numbers[:6]) > 1 else None