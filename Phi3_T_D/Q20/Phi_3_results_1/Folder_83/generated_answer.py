def find_n_th_smallest_num(numbers):
    start_index = 30 if len(numbers) > 30 else 0
    end_index = 300 if len(numbers) > 300 else len(numbers)
    return sorted(numbers[start_index:end_index])[14]