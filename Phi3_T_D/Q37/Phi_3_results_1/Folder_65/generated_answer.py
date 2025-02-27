def filter_chars(s):
    filtered_chars = [c for c in s if not (61 <= ord(c) <= 70 and '0' <= c <= '@')]
    return ''.join(filtered_chars)