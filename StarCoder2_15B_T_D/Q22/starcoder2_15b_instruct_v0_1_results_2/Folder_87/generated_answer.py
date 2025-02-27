def find_sum_of_multiples(n):
    assert isinstance(n, int) and n > 0, 'n must be a positive integer'
    multiples = [i * n for i in range(1, 58)]
    return sum(multiples)