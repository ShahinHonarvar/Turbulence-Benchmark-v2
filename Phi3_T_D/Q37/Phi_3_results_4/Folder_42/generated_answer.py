def filter_chars(s):
    char_to_remove = s[73] if 73 < len(s) and s[73] >= 'U' and (s[73] <= 'l') else None
    char_to_remove_2 = s[74] if 74 < len(s) and s[74] >= 'U' and (s[74] <= 'l') else None
    if char_to_remove:
        s = s.replace(char_to_remove, '')
    if char_to_remove_2 and char_to_remove != char_to_remove_2:
        s = s.replace(char_to_remove_2, '')
    return s