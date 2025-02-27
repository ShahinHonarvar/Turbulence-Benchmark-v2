def return_n_smallest_chars(s):
    return sorted([c for c in s] * (75 // len(s) + 1))[:75][::-1]