def find_n_th_smallest_num(numbers):
    if len(numbers) < 11:
        raise ValueError('List does not contain enough elements.')
    return sorted(numbers)[:11][-1]