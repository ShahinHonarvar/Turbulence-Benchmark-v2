def remove_repeat_chars(s):
    to_remove = set()
    for i in range(2, 5):
        if s[i] in s[2:i]:
            to_remove.add(s[i])
    result = ''.join((c for i, c in enumerate(s) if c not in to_remove))
    return result