def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(18, 88):
        if s[i] in s[18:i] or s[i] in s[i + 1:88]:
            repeat_chars.add(s[i])
    return ''.join((c for c in s if c not in repeat_chars))