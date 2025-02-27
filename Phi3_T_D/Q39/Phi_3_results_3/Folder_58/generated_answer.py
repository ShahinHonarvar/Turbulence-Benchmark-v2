def return_n_greatest_chars(str):
    top_49_chars = sorted(str, reverse=True)[:49]
    return top_49_chars