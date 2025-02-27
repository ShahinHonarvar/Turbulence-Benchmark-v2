def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('A'), ord('b') + 1) if 35 <= i <= 98}
    return ''.join((c for c in s if c not in chars_to_remove))