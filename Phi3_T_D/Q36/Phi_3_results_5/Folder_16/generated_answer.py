def filter_chars(input_str):
    for i in range(331, 713):
        if 'M' < input_str[i] < '_':
            input_str = input_str.replace(input_str[i], '')
    return input_str