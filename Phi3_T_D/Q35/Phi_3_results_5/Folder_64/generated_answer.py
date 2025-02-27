def remove_repeat_chars(s):
    first_six = s[:6]
    seen_chars = set()
    for c in first_six:
        if first_six.count(c) > 1:
            seen_chars.add(c)
    result = ''.join((c for c in s if c not in seen_chars))
    return result