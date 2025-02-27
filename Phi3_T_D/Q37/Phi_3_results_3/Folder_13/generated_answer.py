def filter_chars(s):
    char_range = [i for i in s[124:855] if '9' <= i <= 's']
    return ''.join(filter(lambda x: x not in char_range, s))