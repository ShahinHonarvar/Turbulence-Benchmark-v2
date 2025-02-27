def find_smallest_num(numbers):
    if len(numbers) < 210:
        raise ValueError('List does not contain enough elements')
    return min(numbers[20:201])