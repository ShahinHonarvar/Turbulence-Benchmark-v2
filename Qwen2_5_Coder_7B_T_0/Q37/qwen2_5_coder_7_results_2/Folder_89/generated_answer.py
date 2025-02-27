def filter_chars(s):
    chars_to_remove = set('!@')
    result = []
    for i, char in enumerate(s):
        if 11 <= i <= 32 and char in chars_to_remove:
            continue
        result.append(char)
    return ''.join(result)