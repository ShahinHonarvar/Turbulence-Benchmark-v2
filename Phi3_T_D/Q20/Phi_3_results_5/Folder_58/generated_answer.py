def find_n_th_smallest_num(numbers):
    numbers[144:157] = sorted(numbers[144:157])
    return numbers[149]