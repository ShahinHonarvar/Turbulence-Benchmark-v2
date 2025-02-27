def remove_repeat_chars(s):
    return ''.join([s[i] for i in range(len(s)) if (i < 72 or i > 93) or s[i] not in s[72:93]])