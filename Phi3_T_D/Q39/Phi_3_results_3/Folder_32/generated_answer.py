def return_n_greatest_chars(str):
    chars = sorted(set(str), reverse=True)
    top_eight = sorted(chars[:8])
    return top_eight