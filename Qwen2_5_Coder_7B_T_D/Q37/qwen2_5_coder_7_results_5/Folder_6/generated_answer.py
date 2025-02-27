def filter_chars(s):
    target_chars = 'cdefghijklmn'
    result = ''
    for i, char in enumerate(s):
        if 13 <= i <= 28 and char in target_chars:
            continue
        result += char
    return result