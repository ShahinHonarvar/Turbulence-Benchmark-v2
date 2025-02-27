def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(3, 9):
        if s[i] in s[3:i] or s[i] in s[i + 1:9]:
            repeat_chars.add(s[i])
    result = ''.join((c for c in s if c not in repeat_chars))
    return result