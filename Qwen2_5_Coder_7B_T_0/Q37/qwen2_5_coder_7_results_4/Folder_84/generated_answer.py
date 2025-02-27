def filter_chars(s):
    chars_to_remove = set('6789ABC')
    result = []
    for i, char in enumerate(s):
        if not 138 <= i <= 920 or char not in chars_to_remove:
            result.append(char)
    return ''.join(result)