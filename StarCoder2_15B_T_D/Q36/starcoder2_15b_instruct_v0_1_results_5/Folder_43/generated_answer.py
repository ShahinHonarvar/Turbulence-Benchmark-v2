def filter_chars(input_str):
    return ''.join((c for i, c in enumerate(input_str) if i < 27 or i >= 75 or (c <= 'A' or c >= 'i')))