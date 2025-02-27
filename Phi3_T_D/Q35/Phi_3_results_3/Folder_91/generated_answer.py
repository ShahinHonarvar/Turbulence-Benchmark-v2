def remove_repeat_chars(s):
    exclude_chars = set()
    for i in range(1, 7):
        if s[i] in s[:i]:
            exclude_chars.add(s[i])
    return ''.join([c for c in s if c not in exclude_chars])