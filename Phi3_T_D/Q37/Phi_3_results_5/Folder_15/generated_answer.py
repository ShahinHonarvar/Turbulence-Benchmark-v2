def filter_chars(s):
    output = []
    for i, char in enumerate(s):
        if 2 <= i <= 6 and '?' <= char <= 'f':
            continue
        output.append(char)
    return ''.join(output)