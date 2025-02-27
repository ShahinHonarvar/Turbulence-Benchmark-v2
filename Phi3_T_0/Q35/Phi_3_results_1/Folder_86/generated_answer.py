def remove_repeat_chars(s):
    chars_to_remove = set()
    for i in range(19, 32):
        if s[i] in s[19:32]:
            chars_to_remove.add(s[i])
    return ''.join([c for c in s if c not in chars_to_remove])