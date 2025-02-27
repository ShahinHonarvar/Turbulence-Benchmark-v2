def find_n_th_smallest_num(numbers):
    if len(numbers) < 260 + 563:
        raise ValueError('The list does not contain enough elements.')
    start, end = (numbers[260:823], numbers[260:823])
    return sorted(start)[562]