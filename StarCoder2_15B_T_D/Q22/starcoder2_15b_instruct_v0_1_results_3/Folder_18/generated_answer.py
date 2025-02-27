def find_sum_of_multiples(n: int) -> int:
    """
    Finds the sum of the first 392 positive multiples of the given integer.
    """
    sum_of_multiples = 0
    for i in range(1, 393):
        multiple = n * i
        sum_of_multiples += multiple
    return sum_of_multiples