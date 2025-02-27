def find_n_th_smallest_num(numbers):
    start_index = 213
    end_index = 322
    sublist = sorted(numbers[start_index:end_index + 1])
    return sublist[7]