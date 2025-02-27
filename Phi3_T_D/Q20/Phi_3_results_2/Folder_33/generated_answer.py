def find_n_th_smallest_num(numbers):
    target_slice = numbers[213:323]
    if len(target_slice) < 8:
        return None
    target_slice.sort()
    return target_slice[7]