def remove_repeat_chars(s):
    seen = set()
    result = ''
    for c in s[33:78]:
        if c not in seen:
            seen.add(c)
            result += c
    return result