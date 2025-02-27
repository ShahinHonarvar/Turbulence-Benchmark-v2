def find_sum_of_multiples(n):
    limit = 186
    return sum((n * i for i in range(1, limit + 1)))