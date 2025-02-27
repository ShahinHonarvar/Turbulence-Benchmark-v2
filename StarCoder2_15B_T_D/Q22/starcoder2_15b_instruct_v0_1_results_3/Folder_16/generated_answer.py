def find_sum_of_multiples(n):
    assert isinstance(n, int) and n > 0
    multiples = [i * n for i in range(1, 256)]
    return sum(multiples)