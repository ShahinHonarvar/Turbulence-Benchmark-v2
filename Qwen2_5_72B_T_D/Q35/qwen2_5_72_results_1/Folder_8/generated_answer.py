def remove_repeat_chars(s):
    chars = {}
    for i in range(45, 48):
        if s[i] in chars:
            chars[s[i]] += 1
        else:
            chars[s[i]] = 1
    result = ''.join((c for i, c in enumerate(s) if i < 45 or i >= 48 or chars.get(c, 0) < 2))
    return result