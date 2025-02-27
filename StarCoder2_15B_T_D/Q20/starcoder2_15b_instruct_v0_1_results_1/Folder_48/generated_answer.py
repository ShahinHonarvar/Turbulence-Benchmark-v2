def find_n_th_smallest_num(numbers):
    window = numbers[127:849]
    window.sort()
    return window[9]