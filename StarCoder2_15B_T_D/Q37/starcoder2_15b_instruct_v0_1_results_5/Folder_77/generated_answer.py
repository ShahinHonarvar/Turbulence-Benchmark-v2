def filter_chars(string):
    filtered = [c for c in string if not (384 <= ord(c) <= 411 and '/' <= c <= '8')]
    return ''.join(filtered)