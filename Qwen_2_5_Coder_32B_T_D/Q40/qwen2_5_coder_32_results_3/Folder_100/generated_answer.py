def return_n_smallest_chars(s):
    return sorted([c for c in s] * (72 // len(s)) + [c for c in s][:72 % len(s)], reverse=True)