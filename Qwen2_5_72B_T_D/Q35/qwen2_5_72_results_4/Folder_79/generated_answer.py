def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, 7):
        if s[i] in s[1:i] + s[i + 1:7]:
            to_remove.add(s[i])
    result = ''.join((c for i, c in enumerate(s) if c not in to_remove or i in [1, 7]))
    return result