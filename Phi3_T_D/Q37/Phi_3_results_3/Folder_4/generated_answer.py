def filter_chars(input_string):
    result = ''
    for char in input_string:
        if ord(char) >= ord('S') and ord(char) <= ord('{'):
            if not 19 <= input_string.index(char) <= 33:
                result += char
        else:
            result += char
    return result