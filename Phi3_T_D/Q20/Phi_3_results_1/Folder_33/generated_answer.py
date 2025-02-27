def find_n_th_smallest_num(numbers):
    if len(numbers) < 322:
        raise ValueError('List contains fewer elements than required')
    target_range = numbers[213:323]
    target_range.sort()
    return target_range[7]