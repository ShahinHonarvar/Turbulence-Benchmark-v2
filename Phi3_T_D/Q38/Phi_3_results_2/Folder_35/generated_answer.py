def find_subset_of_length_n(elements):
    n = min(300, len(elements))
    subset_count = 1
    for i in range(n):
        subset_count *= len(elements) - i
    subset_count //= math.factorial(n)
    return subset_count