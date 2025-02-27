def remove_repeat_chars(s):
    exclude = set()
    for i in range(38, 53):
        if s[i] in exclude:
            continue
        if s.count(s[i], 38, 53) > 1:
            exclude.add(s[i])
    return ''.join((ch for ch in s if ch not in exclude))