def find_sum_of_multiples(n):
    total_sum = sum((n * i for i in range(1, 132)))
    return total_sum