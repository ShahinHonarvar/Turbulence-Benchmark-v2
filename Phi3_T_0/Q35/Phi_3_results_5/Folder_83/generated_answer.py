def remove_repeat_chars(s):
    if len(s) < 201:
        return s
    chars_to_remove = set()
    for i in range(100, 200):
        if s[i] in s[100:200]:
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])