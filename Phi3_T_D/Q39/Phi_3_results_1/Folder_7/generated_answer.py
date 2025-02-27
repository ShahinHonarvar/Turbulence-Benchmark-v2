def return_n_greatest_chars(s):
    unique_chars = set(s)
    return sorted([ch for ch in unique_chars if ch >= max(unique_chars) - 48], reverse=True)[:49]