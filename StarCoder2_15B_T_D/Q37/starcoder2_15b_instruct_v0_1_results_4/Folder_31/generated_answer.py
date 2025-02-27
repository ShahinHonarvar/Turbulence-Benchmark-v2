def filter_chars(s):
    chars_to_remove = {chr(i) for i in range(57, 97)}
    result = ''
    for c in s:
        if c not in chars_to_remove:
            result += c
    return result