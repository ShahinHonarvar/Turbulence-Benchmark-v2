def filter_chars(s):
    output = []
    for c in s:
        if c < ':' or c > 'r':
            output.append(c)
    return ''.join(output)