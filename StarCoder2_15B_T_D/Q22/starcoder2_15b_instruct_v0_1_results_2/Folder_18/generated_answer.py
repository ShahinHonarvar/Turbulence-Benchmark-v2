def find_sum_of_multiples(n):
    multiples = [i for i in range(1, 400) if n * i <= 1000]
    return sum(multiples)