def find_second_smallest_num(numbers):
    if len(numbers) <= 1:
        return None
    return sorted(numbers[:2])[1]