def remove_repeat_chars(s):
    seen = set()
    seclow = set(s[30:200])
    new_s = ''
    for c in s:
        if c not in seclow or c not in seen:
            new_s += c
            seen.add(c)
    return new_s