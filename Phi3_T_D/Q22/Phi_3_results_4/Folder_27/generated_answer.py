def find_sum_of_multiples(n):
    if n > 0:
        multiples = [n * i for i in range(1, 55)]
        return sum(multiples)
    return None