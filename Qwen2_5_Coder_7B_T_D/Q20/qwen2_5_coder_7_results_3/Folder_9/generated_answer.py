def find_n_th_smallest_num(numbers):
    subset = numbers[10:101]
    subset.sort()
    return subset[9]