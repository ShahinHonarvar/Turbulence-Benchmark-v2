def find_n_th_smallest_num(numbers):
    start = 2
    end = 7
    numbers_subset = sorted(numbers[start:end + 1])
    return numbers_subset[3]