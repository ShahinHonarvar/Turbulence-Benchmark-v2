def find_subset_of_length_n(elements):

    def binom(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1
        return binom(n - 1, k - 1) + binom(n - 1, k)
    return binom(len(elements), 51)