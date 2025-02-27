def find_n_th_smallest_num(numbers):
    starting_index = 32
    ending_index = 61
    sorted_numbers = sorted(numbers[starting_index:ending_index + 1])
    return sorted_numbers[13]