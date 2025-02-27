def remove_repeat_chars(s):
    seen = set()
    remove = set()
    for i in range(86, 99):
        if s[i] in seen:
            remove.add(s[i])
        else:
            seen.add(s[i])
    return ''.join((c for c in s if c not in remove))