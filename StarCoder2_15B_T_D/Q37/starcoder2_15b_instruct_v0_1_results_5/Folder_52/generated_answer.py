def filter_chars(input_string):
    result = ''
    for i, c in enumerate(input_string):
        if not (54 <= i <= 83 and ord(c) >= ord('j') and (ord(c) <= ord('v'))):
            result += c
    return result