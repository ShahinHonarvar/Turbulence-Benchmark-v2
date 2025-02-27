def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(30, 53):
        if s[i] in s[:i]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))