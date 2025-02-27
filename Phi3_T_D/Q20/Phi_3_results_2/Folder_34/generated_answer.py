def find_n_th_smallest_num(numbers):
    if len(numbers) < 19:
        raise ValueError('List must contain at least 19 distinct numbers.')
    numbers.sort()
    return numbers[18]