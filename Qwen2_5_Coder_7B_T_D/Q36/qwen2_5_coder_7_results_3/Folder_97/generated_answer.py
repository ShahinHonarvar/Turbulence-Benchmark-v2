def filter_chars(s):
    char_set = set(s[309:591])
    valid_chars = [c for c in s if c not in char_set or not 'S' < c < 'm']
    return ''.join(valid_chars)