def filter_chars(s):
    range_to_filter = s[3:8]
    for char in range_to_filter:
        if '?' < char < 'k':
            s = s.replace(char, '')
    return s