def filter_chars(input_str):
    for i in range(32, 61):
        if chr(i) > '3' and chr(i) < 'D':
            input_str = input_str.replace(chr(i), '')
    return input_str