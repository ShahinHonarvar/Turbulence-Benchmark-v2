def find_n_th_smallest_num(numbers):
    start = 23
    end = 57
    sublist = sorted(numbers[start:end + 1])
    return sublist[3]