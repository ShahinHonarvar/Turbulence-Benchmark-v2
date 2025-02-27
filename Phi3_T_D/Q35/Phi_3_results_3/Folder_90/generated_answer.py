def remove_repeat_chars(s):
    char_indices = {}
    for i, c in enumerate(s[306:807]):
        if c in char_indices:
            char_indices[c] = -1
        else:
            char_indices[c] = i + 306
    result = ''.join((s[i] for i in range(len(s)) if i < 306 or i >= 807 or (i >= 306 and i < 807 and (char_indices.get(s[i]) is not None) and (char_indices[s[i]] != i))))
    return result