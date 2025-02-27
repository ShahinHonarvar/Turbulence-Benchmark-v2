def remove_repeat_chars(s):
    return ''.join([s[i] for i in range(len(s)) if (i < 44 or i > 67) or s[i] not in s[45:67]])