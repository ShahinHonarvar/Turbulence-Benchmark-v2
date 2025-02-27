def return_n_greatest_chars(s):
    return sorted([c for c in s] * (75 // len(s) + 1), reverse=True)[:75]