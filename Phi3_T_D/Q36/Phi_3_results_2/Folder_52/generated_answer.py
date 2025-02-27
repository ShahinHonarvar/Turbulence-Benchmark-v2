def filter_chars(input_string):
    if len(input_string) > 56:
        result = input_string[:49]
    else:
        result = input_string
    for char in input_string[49:56]:
        if 'J' > char > 'I':
            result = result.replace(char, '')
    return result