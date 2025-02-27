def return_n_greatest_chars(input_str):
    n = 87
    if len(input_str) < n:
        return sorted(input_str, reverse=True)
    else:
        return sorted(input_str, reverse=True)[n:]