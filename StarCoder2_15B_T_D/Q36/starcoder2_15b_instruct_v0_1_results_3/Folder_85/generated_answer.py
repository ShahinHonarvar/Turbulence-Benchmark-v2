def filter_chars(s):
    output = ''
    for i, c in enumerate(s):
        if 55 < i < 80 and 'S' < c < 's':
            continue
        else:
            output += c
    return output