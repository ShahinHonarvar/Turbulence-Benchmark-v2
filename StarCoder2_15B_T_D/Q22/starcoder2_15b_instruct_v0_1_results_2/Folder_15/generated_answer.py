def find_sum_of_multiples(n: int) -> int:
    multiples = [i * n for i in range(1, 4)]
    return sum(multiples)