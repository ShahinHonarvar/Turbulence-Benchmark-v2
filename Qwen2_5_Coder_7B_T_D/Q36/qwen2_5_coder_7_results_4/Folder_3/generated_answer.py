def filter_chars(s):
    target_chars = [chr(i) for i in range(ord('!') + 1, ord('?'))]
    chars_to_remove = [c for c in s[42:78] if c in target_chars]
    remove_set = set(chars_to_remove)
    return ''.join((c for c in s if c not in remove_set))