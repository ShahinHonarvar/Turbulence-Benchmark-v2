def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(47, 91):
        if s[i] in s[:46] or s[i] in s[91:]:
            repeat_chars.add(s[i])
    return ''.join([c for c in s if c not in repeat_chars])