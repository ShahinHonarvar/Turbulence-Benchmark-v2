def filter_chars(input_string):
    result = []
    for i, char in enumerate(input_string):
        if 33 <= ord(char) <= 70 and '7' <= char <= 'k':
            continue
        result.append(char)
    return ''.join(result)