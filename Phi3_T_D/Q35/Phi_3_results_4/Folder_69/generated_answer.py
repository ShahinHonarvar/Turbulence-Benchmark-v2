def remove_repeat_chars(s):
    char_to_remove = []
    for i in range(39, 43):
        if s[i] in s[39:43]:
            char_to_remove.append(s[i])
    return ''.join([c for c in s if c not in char_to_remove])