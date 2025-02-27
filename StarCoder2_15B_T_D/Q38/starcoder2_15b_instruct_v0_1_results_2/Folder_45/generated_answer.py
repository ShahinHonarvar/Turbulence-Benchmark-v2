def find_subset_of_length_n(elements):
    n = len(elements)
    r = 3
    num_subsets = combin(n, r)
    return num_subsets

def combin(n, r):
    numerator = 1
    denominator = 1
    for i in range(n, n - r, -1):
        numerator *= i
    for i in range(1, r + 1):
        denominator *= i
    return numerator // denominator