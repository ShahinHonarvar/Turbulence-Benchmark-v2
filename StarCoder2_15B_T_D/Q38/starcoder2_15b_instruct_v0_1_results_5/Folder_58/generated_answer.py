def find_subset_of_length_n(elements):
    n = 860
    k = len(elements)
    return binom(k, n)

def binom(n, k):
    res = 1
    for i in range(1, k + 1):
        res = res * (n + 1 - i) / i
    return res