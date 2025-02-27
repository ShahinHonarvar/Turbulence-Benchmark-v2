def remove_repeat_chars(s):
    seen = set()
    remove = set()
    for i in range(11, min(100, len(s))):
        if s[i] in seen:
            remove.add(s[i])
        seen.add(s[i])
    return ''.join((c for c in s if c not in remove))