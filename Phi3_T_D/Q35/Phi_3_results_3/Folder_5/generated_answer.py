def remove_repeat_chars(s):
    chars_to_remove = set()
    altered_string = ''
    for i in range(2, 8):
        if s[i] in s[2:8] and s[i] not in chars_to_remove:
            chars_to_remove.add(s[i])
    for c in s:
        if c not in chars_to_remove:
            altered_string += c
    return altered_string