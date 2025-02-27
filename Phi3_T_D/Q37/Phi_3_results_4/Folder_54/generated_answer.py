def filter_chars(input_string):
    result = []
    for i in range(len(input_string)):
        if 46 <= i <= 85 and input_string[i] >= '-' and (input_string[i] <= 'X'):
            continue
        result.append(input_string[i])
    return ''.join(result)