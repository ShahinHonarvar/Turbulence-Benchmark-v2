def find_sum_of_multiples(n):
    total_sum = 0
    for i in range(1, 465):
        multiple = n * i
        total_sum += multiple
    return total_sum