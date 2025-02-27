def filter_chars(input_string):
    output_string = ''
    start_index = 56
    end_index = 86
    for i in range(len(input_string)):
        if start_index <= i < end_index:
            char = input_string[i]
            if '+' < char < 'w':
                output_string = output_string.replace(char, '')
            else:
                output_string += char
        else:
            output_string += char
    return output_string