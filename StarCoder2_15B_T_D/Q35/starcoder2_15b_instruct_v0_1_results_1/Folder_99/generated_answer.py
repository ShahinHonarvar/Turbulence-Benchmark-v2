def remove_repeat_chars(string):
    seen_chars = {}
    result = ''
    for i, c in enumerate(string):
        if c not in seen_chars:
            seen_chars[c] = i
            result += c
    return result