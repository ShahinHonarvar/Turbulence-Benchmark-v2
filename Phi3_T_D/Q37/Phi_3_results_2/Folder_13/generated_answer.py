def filter_chars(input_str):
    for i in range(124, 855):
        if '9' <= input_str[i] <= 's':
            input_str = input_str.replace(input_str[i], '')
    return input_str