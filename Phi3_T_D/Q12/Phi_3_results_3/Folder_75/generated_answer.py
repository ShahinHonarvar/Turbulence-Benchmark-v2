def find_smallest_num(numbers):
    if len(numbers) > 84 and len(numbers) > 70:
        return min(numbers[70:85])
    else:
        raise ValueError('List must have at least 85 elements to consider position 70 to 84.')