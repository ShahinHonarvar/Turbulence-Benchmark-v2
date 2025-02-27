def find_subset_of_length_n(s):
    n = len(s)
    if n < 36:
        return 0
    k = 36
    return int(scipy.special.comb(n, k))