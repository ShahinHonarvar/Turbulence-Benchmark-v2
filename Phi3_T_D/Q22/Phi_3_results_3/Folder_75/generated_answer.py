def find_sum_of_multiples(n):
    sum_multiples = sum((i * n for i in range(1, 16)))
    return sum_multiples