def filter_chars(s):
    altered_chars = [ch for ch in s if not (54 <= s.index(ch) <= 62 and ')' <= ch <= '9')]
    return ''.join(altered_chars)