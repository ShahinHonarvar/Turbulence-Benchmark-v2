def find_second_smallest_num(numbers):
    if len(numbers) < 9:
        return None
    sorted_num = sorted(numbers[:9])
    return sorted_num[1]