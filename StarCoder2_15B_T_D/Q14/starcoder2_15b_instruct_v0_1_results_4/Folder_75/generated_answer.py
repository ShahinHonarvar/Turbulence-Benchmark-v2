def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    sorted_sublist = sorted(numbers[12:93])
    return sorted_sublist[1]