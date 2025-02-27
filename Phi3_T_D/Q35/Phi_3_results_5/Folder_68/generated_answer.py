def remove_repeat_chars(s):
    for i in range(10):
        if s.count(s[i]) > 1 and s[i] not in s[i + 1:9]:
            s = s.replace(s[i], '')
    return s