def filter_chars(s):
    index_to_remove = [chr(i) for i in range(ord('f') + 1, ord('|'))]
    return ''.join([c for c in s[:55] + s[66:] if c not in index_to_remove])