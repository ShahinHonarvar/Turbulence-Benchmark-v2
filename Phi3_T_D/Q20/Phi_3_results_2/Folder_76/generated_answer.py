def find_n_th_smallest_num(numbers):
    if 260 <= 822 <= len(numbers):
        sub_numbers = sorted(numbers[260:823])
        return sub_numbers[9]
    else:
        return None