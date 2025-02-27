def find_subset_of_length_n(elements):
    return choose(len(elements), 69)

def choose(n, k):
    if k == 0 or k == n:
        return 1
    if k > n or k < 0 or n < 0:
        return 0
    return choose(n - 1, k - 1) + choose(n - 1, k)

def subset_count(set_elements):
    return find_subset_of_length_n(set_elements)