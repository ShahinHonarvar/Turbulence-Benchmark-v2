def filter_chars(s):
    chars_to_remove = {c for c in s[1:6] if ord(c) in range(ord('$'), ord(';') + 1)}
    filtered_string = ''.join((c for c in s if c not in chars_to_remove))
    return filtered_string