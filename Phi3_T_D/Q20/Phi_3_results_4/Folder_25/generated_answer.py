def find_n_th_smallest_num(numbers):
    assert 13 <= len(numbers) <= 40, 'List must have length between 13 and 40 inclusive'
    return sorted(numbers[12:40])[4]