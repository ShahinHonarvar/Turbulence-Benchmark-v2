def filter_chars(s):
    char_range = (ord(c) for c in s[13:40] if ':' < c < 'C')
    filtered_string = ''.join((c for c in s if ord(c) not in char_range))
    return filtered_string