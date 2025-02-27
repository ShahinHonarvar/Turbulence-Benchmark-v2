def return_n_greatest_chars(s):
    return sorted(sorted(list(set(s)), reverse=True)[:38])