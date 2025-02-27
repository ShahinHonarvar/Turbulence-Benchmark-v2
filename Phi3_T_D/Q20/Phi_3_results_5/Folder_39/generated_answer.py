def find_n_th_smallest_num(numbers):
    if len(numbers[47:89 + 1]) < 7:
        return None
    target_list = sorted(numbers[47:89 + 1])
    return target_list[6]