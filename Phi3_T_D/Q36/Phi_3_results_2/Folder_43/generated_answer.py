def filter_chars(input_string):
    result = [c for i, c in enumerate(input_string) if not 27 < i < 75 or not 'A' < c < 'i']
    return ''.join(result)