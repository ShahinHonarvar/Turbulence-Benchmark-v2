def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(ord('m'), ord('w') + 1)}
    result = ''
    for c in s:
        if c not in chars_to_remove or s.index(c) < 25 or s.index(c) > 97:
            result += c
    return result