def remove_repeat_chars(s):
    seen = set()
    result = ''
    for i in range(4):
        if s[i] not in seen and s.count(s[i], 0, i) == 0:
            result += s[i]
            seen.add(s[i])
    return result