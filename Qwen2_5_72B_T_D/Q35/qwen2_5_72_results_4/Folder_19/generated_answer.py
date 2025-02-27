def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, 4):
        if s[i] in s[1:i] + s[i + 1:4]:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))