def filter_chars(s):
    if len(s) < 10:
        return s
    target_range = s[3:9]
    chars_to_filter = [char for char in target_range if '*' < char < 'E']
    for char in chars_to_filter:
        s = s.replace(char, '')
    return s