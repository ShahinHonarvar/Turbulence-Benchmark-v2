def remove_repeat_chars(s):
    chars_to_remove = set(s[1:4])
    return ''.join((c for c in s if c not in chars_to_remove or chars_to_remove.remove(c) or True))