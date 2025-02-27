def filter_chars(input_string):
    result = []
    for char in input_string:
        if ord(char) >= ord('_') and ord(char) <= ord('o'):
            if not 71 <= input_string.index(char) <= 96:
                result.append(char)
    return ''.join(result)