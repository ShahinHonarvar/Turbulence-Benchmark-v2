def find_sum_of_multiples(n):
    multiples = [i for i in range(1, 290) if n * i <= 289]
    return sum(multiples)