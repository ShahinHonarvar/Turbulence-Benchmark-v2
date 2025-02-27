def filter_chars(s):
    altered_chars = [c for c in s if not 318 <= ord(c) <= 337 or 'B' <= c <= 'z']
    return ''.join(altered_chars)