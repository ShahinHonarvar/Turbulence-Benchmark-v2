def remove_repeat_chars(s):
    s = list(s)
    seen = set()
    for i in range(32, 98):
        if s[i] in seen:
            del s[i]
        else:
            seen.add(s[i])
    return ''.join(s)