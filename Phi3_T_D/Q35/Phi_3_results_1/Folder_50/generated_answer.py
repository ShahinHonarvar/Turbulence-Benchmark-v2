def remove_repeat_chars(s):
    char_freq = {}
    new_s = []
    for i, c in enumerate(s[13:75]):
        if c not in char_freq:
            char_freq[c] = i
            new_s.append(c)
        else:
            char_freq[c] = -1
    return ''.join(new_s) + s[75:]