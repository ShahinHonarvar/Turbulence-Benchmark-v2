def remove_repeat_chars(s):
    to_remove = set()
    for i in range(1, 6):
        if s.count(s[i]) > 1:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))