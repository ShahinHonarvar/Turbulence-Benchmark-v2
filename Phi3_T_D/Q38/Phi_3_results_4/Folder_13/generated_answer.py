def find_subset_of_length_n(elements):
    n = 801
    if len(elements) < n:
        return 0
    result = 1
    for i in range(len(elements), len(elements) - n, -1):
        result *= i
        result //= i - n + 1
    return result