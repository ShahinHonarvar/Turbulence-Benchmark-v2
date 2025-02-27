def return_n_greatest_chars(input_str):
    sorted_chars = sorted(input_str, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:21]