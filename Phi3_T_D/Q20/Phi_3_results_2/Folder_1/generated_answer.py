def find_n_th_smallest_num(numbers):
    slice_range = numbers[17:38 + 1]
    slice_range.sort()
    return slice_range[10]