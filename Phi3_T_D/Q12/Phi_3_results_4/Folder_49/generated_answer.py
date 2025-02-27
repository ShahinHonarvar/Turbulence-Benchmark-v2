def find_smallest_num(numbers):
    if len(numbers) > 80:
        return min(numbers[80:81])
    else:
        raise ValueError('List too short.')