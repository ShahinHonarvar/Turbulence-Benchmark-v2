def find_n_th_smallest_num(numbers):
    start = 43
    end = 80
    if len(numbers) < end:
        raise ValueError('List does not contain enough elements from index 43 to 80')
    sorted_numbers = sorted(numbers[start:end + 1])
    return sorted_numbers[5]