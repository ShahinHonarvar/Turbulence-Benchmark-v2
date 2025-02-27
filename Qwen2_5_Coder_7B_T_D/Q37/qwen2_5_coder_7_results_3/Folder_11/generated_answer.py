def filter_chars(s):
    chars_to_remove = set('-.0123456789:;<=>?@[\\\\]^_`{|}~')
    result = ''
    for i, char in enumerate(s):
        if 29 <= i <= 97 and char in chars_to_remove:
            continue
        result += char
    return result