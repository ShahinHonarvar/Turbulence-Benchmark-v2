def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 69:
        return 0
    result = 1
    for i in range(n, n - 69, -1):
        result *= i
    for i in range(1, 69):
        result //= i
    return result