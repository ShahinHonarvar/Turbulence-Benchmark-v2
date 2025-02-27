def remove_repeat_chars(s):
    char_indices = [i for i, c in enumerate(s) if s.count(c) > 1]
    result = ''
    for i, c in enumerate(s):
        if 45 < i < 48 and i in char_indices:
            continue
        result += c
    return result