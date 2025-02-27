def find_n_th_smallest_num(numbers):
    n = 7
    if 2 <= n <= len(numbers) - 1:
        return sorted(numbers[2:9])[n - 1]
    else:
        return None