def return_n_smallest_chars(s):
    return sorted([c for c in s] * (87 // len(s) + 1))[:87][::-1]