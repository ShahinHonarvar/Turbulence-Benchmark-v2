def remove_repeat_chars(s):
    seen = set()
    to_remove = set()
    for i in range(14, 70):
        if s[i] in seen:
            to_remove.add(s[i])
        else:
            seen.add(s[i])
    return ''.join((c for c in s if c not in to_remove))