def find_subset_of_length_n(elements):

    def count_combinations(n, r):

        def factorial(x):
            return 1 if x == 0 else x * factorial(x - 1)
        return factorial(n) // (factorial(n - r) * factorial(r))
    return count_combinations(len(elements), 59) if len(elements) >= 59 else 0