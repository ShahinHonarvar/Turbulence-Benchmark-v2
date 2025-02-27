def find_sum_of_multiples(n):
    multiples = [i for i in range(1, 47) for j in range(1, n + 1) if i * j == n]
    return sum(multiples)