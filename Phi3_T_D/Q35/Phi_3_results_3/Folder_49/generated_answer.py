def remove_repeat_chars(s):
    if len(s) < 111:
        return s
    char_set = set(s[90:200])
    result = [s[i] for i in range(len(s)) if s[i] not in char_set or s[i] not in s[90:199] or i < 90 or (i > 199)]
    return ''.join(result)