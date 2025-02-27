def remove_repeat_chars(s):
    if len(s) <= 93:
        return s
    chars_to_remove = set()
    new_string = ''
    for i in range(20, 93):
        if s[i] in s[20:93] and s[i] not in chars_to_remove:
            chars_to_remove.add(s[i])
        elif s[i] in chars_to_remove:
            continue
        new_string += s[i]
    return new_string