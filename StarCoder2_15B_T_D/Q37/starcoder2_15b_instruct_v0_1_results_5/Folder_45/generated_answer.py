def filter_chars(input_string):
    output_string = ''
    for char in input_string:
        if char >= '.' and char <= 'b' and (input_string.index(char) < 72 or input_string.index(char) > 94):
            continue
        else:
            output_string += char
    return output_string