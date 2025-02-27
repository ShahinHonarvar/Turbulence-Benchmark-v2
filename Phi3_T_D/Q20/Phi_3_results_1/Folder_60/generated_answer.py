def find_n_th_smallest_num(numbers):
    sliced_numbers = numbers[15:74]
    sliced_numbers.sort()
    return sliced_numbers[0]