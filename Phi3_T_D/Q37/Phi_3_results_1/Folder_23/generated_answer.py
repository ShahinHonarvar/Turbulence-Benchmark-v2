def filter_chars(s):
    filtered_chars = ''.join([char for i, char in enumerate(s) if not (51 <= i <= 77 and 'V' <= char <= 'Y')])
    return filtered_chars