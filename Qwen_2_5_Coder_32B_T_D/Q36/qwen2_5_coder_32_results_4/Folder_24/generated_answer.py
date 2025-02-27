def filter_chars(s):
    chars_to_remove = set(s[11:15])
    result = []
    for char in s:
        if char not in chars_to_remove or not 't' < char < 'v':
            result.append(char)
    return ''.join(result)