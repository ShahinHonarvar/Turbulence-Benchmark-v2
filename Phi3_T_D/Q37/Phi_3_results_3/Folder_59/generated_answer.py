def filter_chars(s):
    char_to_filter = s[2:4]
    filtered_chars = ''.join([c for c in char_to_filter if not 5 <= ord(c) <= ord('_')])
    return s.replace(char_to_filter, filtered_chars)