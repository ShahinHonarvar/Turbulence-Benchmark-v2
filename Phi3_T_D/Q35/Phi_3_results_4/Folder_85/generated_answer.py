def remove_repeat_chars(s):
    s_len = len(s)
    if s_len <= 8:
        return s
    char_dict = {}
    for i in range(2, 8):
        if s[i] in char_dict:
            continue
        char_dict[s[i]] = True
    new_s = [char for char in s if char not in char_dict]
    return ''.join(new_s)