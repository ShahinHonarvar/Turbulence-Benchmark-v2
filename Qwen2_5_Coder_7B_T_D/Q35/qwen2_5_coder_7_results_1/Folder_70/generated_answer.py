def remove_repeat_chars(s):
    return ''.join([s[i] for i in range(len(s)) if (i < 43 or i >= 70) or s[i] not in s[43:70]])