def remove_repeat_chars(s):
    repeat_chars = set()
    for i in range(20, 51):
        if s[i] in s[20:51]:
            repeat_chars.add(s[i])
    return ''.join([c for c in s if c not in repeat_chars])