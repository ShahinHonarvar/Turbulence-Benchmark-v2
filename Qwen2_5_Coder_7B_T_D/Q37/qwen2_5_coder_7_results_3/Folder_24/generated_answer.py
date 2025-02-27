def filter_chars(s):
    chars_to_filter = set('23456789ABCDEFGHJKLMNPQRSTUVWXYZ')
    result = ''
    for i, char in enumerate(s):
        if not 36 <= i <= 79 or char not in chars_to_filter:
            result += char
    return result