def remove_repeat_chars(s):
    to_remove = set()
    for i in range(2, 6):
        if s[i] in s[2:i] + s[i + 1:6]:
            to_remove.add(s[i])
    result = ''.join((c for c in s if c not in to_remove))
    return result