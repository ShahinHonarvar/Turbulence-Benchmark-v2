def find_n_th_smallest_num(numbers):
    subset = numbers[30:301]
    subset.sort()
    return subset[14]