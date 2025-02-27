def find_n_th_smallest_num(numbers):
    target_index = 9
    start_index = 51
    end_index = 71
    sublist = sorted(numbers[start_index:end_index + 1])
    return sublist[target_index - 1]