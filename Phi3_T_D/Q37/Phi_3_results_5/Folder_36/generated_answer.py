def filter_chars(s):
    if 259 <= len(s) <= 502:
        chars_to_remove = [chr(i) for i in range(ord(','), ord('3') + 1)]
        return ''.join((c for c in s[259:503] if c not in chars_to_remove)) + s[503:]
    return s