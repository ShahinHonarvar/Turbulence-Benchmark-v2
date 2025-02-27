def find_second_smallest_num(numbers):
    if len(numbers) < 85 or len(set(numbers[70:85])) < 2:
        return None
    subset = sorted(numbers[70:85])
    return subset[1]