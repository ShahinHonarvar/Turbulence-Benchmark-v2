def find_n_th_smallest_num(numbers, index=470, n=9, end_index=654):
    sliced_numbers = sorted(numbers[index:end_index + 1])
    return sliced_numbers[n - 1]