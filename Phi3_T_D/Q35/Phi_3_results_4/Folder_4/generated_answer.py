def remove_repeat_chars(s):
    char_mask = [False] * len(s)
    for i in range(50, 73):
        char_mask[i] = s[i] in s[50:73]
    result = [s[i] for i in range(len(s)) if not char_mask[i]]
    return ''.join(result)