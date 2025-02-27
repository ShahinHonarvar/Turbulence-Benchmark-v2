def find_n_th_smallest_num(numbers):
    start, end, n = (12, 90, 17)
    sublist = sorted(numbers[start - 1:end])
    return sublist[n - 1]