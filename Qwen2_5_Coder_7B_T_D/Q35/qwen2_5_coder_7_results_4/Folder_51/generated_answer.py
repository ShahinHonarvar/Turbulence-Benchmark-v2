def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(6, 9):
        if s[i] in s[6:9] and s[i] not in repeat_chars:
            repeat_chars.add(s[i])
    return ''.join([char for char in s if char not in repeat_chars])