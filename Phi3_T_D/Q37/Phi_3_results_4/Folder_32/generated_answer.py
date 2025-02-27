def filter_chars(s):
    filtered_string = ''.join((c for i, c in enumerate(s) if not (23 <= i <= 89 and 'w' <= c <= '{')))
    return filtered_string