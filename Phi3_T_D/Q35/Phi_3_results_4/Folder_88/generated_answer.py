def remove_repeat_chars(s):
    if not s or len(s) < 10:
        return s
    s = list(s)
    seen = set()
    for i in range(3, 9):
        if s[i] in seen:
            s = [c for c in s if c != s[i]]
        else:
            seen.add(s[i])
    return ''.join(s)