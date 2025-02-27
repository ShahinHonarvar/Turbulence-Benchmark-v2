def filter_chars(s):
    target_range = s[41:80]
    filtered_chars = [c for c in target_range if not 'f' <= c <= '|']
    return ''.join(filtered_chars)