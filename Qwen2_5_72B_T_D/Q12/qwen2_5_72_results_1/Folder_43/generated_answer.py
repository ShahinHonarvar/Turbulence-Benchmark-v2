def find_smallest_num(numbers):
    if len(numbers) > 23:
        return min(numbers[23:24])
    else:
        return None