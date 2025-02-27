def filter_chars(string):
    output = []
    for char in string:
        if char <= '!' or char >= '}':
            output.append(char)
    return ''.join(output)