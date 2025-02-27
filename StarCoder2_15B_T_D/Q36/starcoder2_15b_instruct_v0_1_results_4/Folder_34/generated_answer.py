def filter_chars(s):
    chars = [c for c in s[10:79] if ord(c) > ord('?') and ord(c) < ord('m')]
    return ''.join(chars)