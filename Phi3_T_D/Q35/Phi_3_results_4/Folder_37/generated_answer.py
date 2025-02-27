def remove_repeat_chars(s):
    if len(s) < 8:
        return s
    char_to_remove = set()
    for i in range(2, 7):
        if s[i] in s[2:i] or s[i] in s[i + 1:7]:
            char_to_remove.add(s[i])
    return ''.join([c for c in s if c not in char_to_remove])