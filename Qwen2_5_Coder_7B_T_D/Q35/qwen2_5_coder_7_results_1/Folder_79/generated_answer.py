def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(1, 7):
        if s[i] in s[1:7] and s[i] not in repeat_chars:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))