def filter_chars(input_str):
    valid_chars = ''
    start_index = 23
    end_index = 45
    for i in range(start_index, end_index):
        if '3' < input_str[i] < 'I':
            valid_chars += input_str[i]
        else:
            valid_chars += input_str[i]
    return valid_chars