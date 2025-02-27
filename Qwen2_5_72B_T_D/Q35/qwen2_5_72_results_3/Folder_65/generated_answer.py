def remove_repeat_chars(s):
    to_remove = set()
    for i in range(51, 76):
        if s[i] in s[51:i] or s[i] in s[i + 1:76]:
            to_remove.add(s[i])
    result = ''.join((c for i, c in enumerate(s) if c not in to_remove or not 51 <= i < 76))
    return result