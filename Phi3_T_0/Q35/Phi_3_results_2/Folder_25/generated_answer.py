def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(37, 43):
        if s[i] in s[37:43]:
            chars_to_remove.add(s[i])
    return ''.join((c for c in s if c not in chars_to_remove))