def return_n_smallest_chars(s):
    return sorted([c for c in s] * (88 // len(s) + 1))[:88][::-1]