def find_n_th_smallest_num(numbers):
    if len(numbers[12:41]) < 5:
        return None
    sorted_numbers = sorted(numbers[12:41])
    return sorted_numbers[4]