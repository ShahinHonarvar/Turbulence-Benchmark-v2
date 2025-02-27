def find_sum_of_multiples(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    total = sum([n * i for i in range(1, 473)])
    return total