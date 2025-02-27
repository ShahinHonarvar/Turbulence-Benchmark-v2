def find_subset_of_length_n(elements_set):
    if len(elements_set) < 380:
        return 0
    n = len(elements_set)

    def combinations(n, r):
        r = min(r, n - r)
        numerator = denominator = 1
        for i in range(r):
            numerator *= n
            n -= 1
            denominator *= i + 1
        return numerator // denominator
    return combinations(n, 380)