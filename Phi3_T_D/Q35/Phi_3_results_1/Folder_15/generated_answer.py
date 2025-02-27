def remove_repeat_chars(s):
    seen = set()
    res = []
    for i in range(4):
        if s[i] not in seen:
            seen.add(s[i])
        else:
            res = [c for c in res if c != s[i]]
    return ''.join(res)