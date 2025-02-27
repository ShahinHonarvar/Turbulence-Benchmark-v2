def return_n_smallest_chars(input_str):
    smallest_chars = sorted(input_str, key=ord)[:37]
    return sorted(smallest_chars, reverse=True)