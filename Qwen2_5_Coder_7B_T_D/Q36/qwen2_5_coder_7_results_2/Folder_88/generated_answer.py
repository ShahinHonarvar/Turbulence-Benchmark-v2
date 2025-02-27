def filter_chars(s):
    if len(s) < 81:
        return s
    char_to_filter = s[78:81]
    for char in char_to_filter:
        if char > 'S' and char < '[':
            s = s.replace(char, '')
    return s