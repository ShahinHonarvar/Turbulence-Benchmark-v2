def filter_chars(s):
    target_range_str = s[31:73]
    chars_to_filter = [c for c in target_range_str if 'M' < c < 'j']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s