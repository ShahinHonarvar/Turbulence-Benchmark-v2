def find_sum_of_multiples(n):
    total = sum((n * i for i in range(1, 148)))
    return total