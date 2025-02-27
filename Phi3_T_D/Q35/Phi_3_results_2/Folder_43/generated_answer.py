def remove_repeat_chars(s):
    start, end = (10, 28)
    to_remove = set()
    for i in range(start, end):
        if s[i] in s[start:i] and s[i] not in to_remove:
            to_remove.add(s[i])
    return ''.join((c for c in s if c not in to_remove))