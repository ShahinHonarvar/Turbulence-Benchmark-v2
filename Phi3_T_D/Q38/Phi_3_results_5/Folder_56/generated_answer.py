def find_subset_of_length_n(elements):
    N = 60
    total_subsets = 1
    for i in range(N):
        total_subsets *= len(elements) - i
    total_subsets //= math.factorial(N)
    return total_subsets