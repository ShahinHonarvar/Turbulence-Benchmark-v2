def remove_repeat_chars(s):
    altered_s = ''
    seen = set()
    for i in range(45, 91):
        if s[i] not in seen:
            altered_s += s[i]
            seen.add(s[i])
    return altered_s