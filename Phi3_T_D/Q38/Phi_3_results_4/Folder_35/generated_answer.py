import math

def find_subset_of_length_n(s):
    count = 0
    n = len(s)
    k = 300
    return math.comb(n, k) if n >= k else 0