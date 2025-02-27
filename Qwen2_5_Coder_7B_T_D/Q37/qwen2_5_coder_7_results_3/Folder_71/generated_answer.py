def filter_chars(s):
    to_remove = set('0123456789k')
    result = []
    for char in s:
        if not 32 <= ord(char) <= 46 or char not in to_remove:
            result.append(char)
    return ''.join(result)