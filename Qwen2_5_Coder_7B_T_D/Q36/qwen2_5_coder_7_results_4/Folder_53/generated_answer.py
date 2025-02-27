def filter_chars(s):
    char_set = {chr(i) for i in range(91, 119) if chr(i) > 'j' and chr(i) < 'w'}
    return ''.join((c for c in s if c not in char_set))