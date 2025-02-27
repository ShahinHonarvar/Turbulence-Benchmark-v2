def find_sum_of_multiples(n):
    total_sum = 0
    if n <= 0:
        return 0
    for i in range(1, 474 + 1):
        total_sum += n * i
    return total_sum