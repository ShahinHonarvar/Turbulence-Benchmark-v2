def find_sum_of_multiples(n):
    multiples = [i for i in range(1, 97) if n * i > 0]
    return sum(multiples)