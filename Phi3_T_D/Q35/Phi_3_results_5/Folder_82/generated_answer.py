def remove_repeat_chars(s):
    seen = set()
    out = []
    for i, c in enumerate(s[30:200]):
        if c in seen:
            continue
        seen.add(c)
        out.append(c)
    return s[:30] + ''.join(out) + s[200:]