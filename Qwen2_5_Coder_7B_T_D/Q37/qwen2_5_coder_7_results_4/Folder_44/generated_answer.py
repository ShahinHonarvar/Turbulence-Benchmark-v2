def filter_chars(s):
    chars_to_remove = set('2345678')
    result = ''
    for i, char in enumerate(s):
        if i < 21 or i > 43 or char not in chars_to_remove:
            result += char
    return result