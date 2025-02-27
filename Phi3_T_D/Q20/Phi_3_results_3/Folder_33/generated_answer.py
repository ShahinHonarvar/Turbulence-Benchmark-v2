def find_n_th_smallest_num(numbers, start=213, end=322, n=8):
    idx_sorted_list = sorted(range(start, end + 1), key=lambda i: numbers[i])
    return numbers[idx_sorted_list[n - 1]]