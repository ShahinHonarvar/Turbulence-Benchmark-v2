def remove_repeat_chars(s):
    return ''.join([s[i] for i in range(len(s)) if s[i] not in s[1:4] or i >= 4])