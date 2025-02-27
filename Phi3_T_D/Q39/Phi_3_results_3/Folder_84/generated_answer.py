def return_n_greatest_chars(str):
    sorted_chars = sorted(str)
    return sorted_chars[-10:][::-1]