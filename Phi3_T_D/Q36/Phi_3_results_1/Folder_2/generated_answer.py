def filter_chars(s):
    s = [c for c in s if 421 < ord(c) < 854 or ord(c) <= ord('D') or ord(c) >= ord('J')]
    return ''.join(s)