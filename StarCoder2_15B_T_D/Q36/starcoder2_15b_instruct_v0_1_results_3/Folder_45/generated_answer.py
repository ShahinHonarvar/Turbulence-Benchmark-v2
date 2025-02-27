def filter_chars(s):
    filtered = [c for c in s if c <= '!' or c >= 's']
    return ''.join(filtered)