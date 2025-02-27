def find_sum_of_multiples(num):
    """
    Function to find the sum of the first 19 positive multiples of a given number.
    """
    total = 0
    for i in range(1, 20):
        total += num * i
    return total