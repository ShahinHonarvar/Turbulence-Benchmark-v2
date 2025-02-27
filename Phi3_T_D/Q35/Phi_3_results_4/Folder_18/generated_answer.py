def remove_repeat_chars(s):
    char_to_remove = set()
    for i in range(56, 90):
        if s[i] in s[56:i] or s[i] in s[i + 1:90]:
            char_to_remove.add(s[i])
    return ''.join([char for char in s if char not in char_to_remove])