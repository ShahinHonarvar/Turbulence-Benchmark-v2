def filter_chars(string):
    result = []
    for char in string:
        if char > '#' and char < 'T':
            continue
        result.append(char)
    return ''.join(result)