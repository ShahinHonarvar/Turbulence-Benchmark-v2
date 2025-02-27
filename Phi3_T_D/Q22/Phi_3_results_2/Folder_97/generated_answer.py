def find_sum_of_multiples(n):
    limit = 210
    total_sum = sum(range(n, n * limit + 1, n))
    return total_sum