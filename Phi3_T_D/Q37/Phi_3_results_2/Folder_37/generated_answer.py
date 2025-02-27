def filter_chars(input_str):
    altered_str = input_str[:17] + ''.join(['' if 'O' <= c <= '^' and 17 <= i <= 63 else c for i, c in enumerate(input_str[17:64])]) + input_str[64:]
    return altered_str