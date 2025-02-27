def find_sum_of_multiples(num):
    """Returns the sum of the first 47 positive multiples of a given number."""
    total_sum = 0
    for i in range(1, 48):
        total_sum += num * i
    return total_sum