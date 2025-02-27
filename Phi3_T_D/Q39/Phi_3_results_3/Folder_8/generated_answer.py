def return_n_greatest_chars(string):
    if len(string) <= 83:
        return sorted(string)
    top_chars = sorted(string)[-83:]
    return sorted(top_chars)