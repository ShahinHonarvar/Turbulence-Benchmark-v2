def filter_chars(input_string):
    output_list = []
    for char in input_string:
        if char <= 'J' or char >= 'X':
            output_list.append(char)
    return ''.join(output_list)