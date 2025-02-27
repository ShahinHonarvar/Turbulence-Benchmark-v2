def remove_repeat_chars(s):
    return ''.join([char for i, char in enumerate(s) if i not in range(77, 84) or s[i] not in s[77:84]])