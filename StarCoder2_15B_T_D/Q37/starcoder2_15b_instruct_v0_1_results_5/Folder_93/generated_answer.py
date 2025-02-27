def filter_chars(s):
    filtered_chars = [c for c in s[38:70] if not 'H' <= c <= 'e']
    return ''.join(filtered_chars)