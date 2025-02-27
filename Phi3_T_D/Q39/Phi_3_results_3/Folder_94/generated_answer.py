def return_n_greatest_chars(input_str):
    unique_chars = sorted(set(input_str), reverse=True)[:87]
    return unique_chars[:87]