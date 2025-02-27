def remove_repeat_chars(s):
    unique_chars = set()
    for i in range(43, 70):
        if s[i] not in unique_chars:
            unique_chars.add(s[i])
        else:
            s = s.replace(s[i], '')
    return s[43:70]