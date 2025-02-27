def filter_chars(s):
    modified_chars = [c for c in s[:672] + s[709:] if ord(c) < ord('X') or ord(c) > ord('}')]
    return ''.join(modified_chars)