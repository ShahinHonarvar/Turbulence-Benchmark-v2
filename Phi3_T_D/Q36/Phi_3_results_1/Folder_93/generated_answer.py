def filter_chars(s):
    altered_chars = set()
    new_s = [c for c in s if (not 52 <= ord(c) < 88 or (ord(c) > ord('&') and ord(c) < ord('c'))) or c in altered_chars or altered_chars.add(c)]
    return ''.join(new_s)