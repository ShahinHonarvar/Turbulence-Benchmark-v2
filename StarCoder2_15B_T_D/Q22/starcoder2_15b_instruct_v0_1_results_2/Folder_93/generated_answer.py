def find_sum_of_multiples(num):
    """Find the sum of the first 66 positive multiples of a given number."""
    total = 0
    for i in range(1, 67):
        total += num * i
    return total