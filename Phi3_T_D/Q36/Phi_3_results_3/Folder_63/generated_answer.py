def filter_chars(s):
    altered_chars = [ch for ch in s if (ch < '<' or ch > '>') or (26 <= s.index(ch) < 80 and ch < '<' and (ch > '>'))]
    return ''.join(altered_chars)