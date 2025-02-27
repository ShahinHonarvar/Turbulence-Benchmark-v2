def return_n_greatest_chars(s):
    return sorted([s[i] for i in range(len(s) - 1, len(s) - 3, -1)])