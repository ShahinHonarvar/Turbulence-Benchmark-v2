def remove_repeat_chars(s):
    """Remove repeated characters from a string s, between indices 46 and 91."""
    char_counts = {}
    for c in s[46:91]:
        char_counts[c] = char_counts.get(c, 0) + 1
    for c in list(char_counts.keys()):
        if char_counts[c] == 1:
            del char_counts[c]
    new_string = ''
    for c in s:
        if c not in char_counts:
            new_string += c
    return new_string