def find_subset_of_length_n(elements):
    n = 60
    elements_length = len(elements)
    return 1 if n > elements_length else choose(elements_length + n - 1, n)

def choose(n, k):
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    numerator = denominator = 1
    i_max = k
    for i in range(i_max):
        numerator *= n - i
        denominator *= i + 1
    return numerator // denominator