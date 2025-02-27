def find_largest_num(numbers):
    max_num = None
    for i in range(25, 88):
        if max_num is None or numbers[i] > max_num:
            max_num = numbers[i]
    return max_num