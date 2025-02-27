def filter_chars(s):
    chars_to_remove = set('ghijklmnopqrstu')
    result = []
    for i, char in enumerate(s):
        if not 27 <= i <= 29 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)