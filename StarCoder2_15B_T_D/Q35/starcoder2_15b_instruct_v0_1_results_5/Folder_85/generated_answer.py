def remove_repeat_chars(s):
    char_dict = {}
    for i, c in enumerate(s):
        if c not in char_dict:
            char_dict[c] = [i]
        else:
            char_dict[c].append(i)
    for c, indices in char_dict.items():
        if len(indices) > 1 and 1 < min(indices) < len(s) - 1:
            s = s.replace(c, '')
    return s