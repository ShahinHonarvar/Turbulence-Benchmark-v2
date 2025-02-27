def remove_repeat_chars(s):
    s = s[462:995]
    seen = set()
    result = []
    for c in s:
        if c not in seen:
            seen.add(c)
            result.append(c)
    return s[:462] + ''.join(result) + s[995:]