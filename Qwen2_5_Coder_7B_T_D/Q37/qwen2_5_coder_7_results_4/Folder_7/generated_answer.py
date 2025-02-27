def filter_chars(s):
    chars_to_remove = set([chr(i) for i in range(ord('>'), ord('_') + 1)])
    result = ''.join([c for c in s if c not in chars_to_remove if 521 <= s.index(c) <= 722])
    return result