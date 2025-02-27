def remove_repeat_chars(s):
    char_positions = [i for i, char in enumerate(s[81:86]) if s.count(char) > 1]
    for pos in char_positions:
        s = s.replace(s[pos:pos + 1], '')
    return s