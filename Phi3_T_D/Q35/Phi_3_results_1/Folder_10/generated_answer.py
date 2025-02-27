def remove_repeat_chars(s):
    char_positions = {}
    for i, c in enumerate(s[36:54]):
        if c in char_positions:
            char_positions[c] = -1
        else:
            char_positions[c] = i + 36
    altered_chars = ''.join([c for i, c in enumerate(s) if c not in char_positions or char_positions[c] != -1])
    return altered_chars