def remove_repeat_chars(s):
    char_to_remove = set()
    for i in range(72, 93):
        if s[i] in s[72:93]:
            char_to_remove.add(s[i])
    return ''.join([char for char in s if char not in char_to_remove])