def return_n_smallest_chars(s):
    return sorted([c for c in s] * (84 // len(s) + 1))[:84][::-1]