def filter_chars(input_string):
    substr_from = 78
    substr_to = 81
    if len(input_string) < substr_to and substr_to > 0:
        substr = input_string[substr_from:substr_to]
        start_char = 'S'
        end_char = '['
        new_string = ''
        for i in range(substr_from):
            if substr[i] > start_char and substr[i] < end_char:
                continue
            else:
                new_string += input_string[i]
        for i in range(substr_to, len(input_string)):
            if input_string[i] == substr[i % (substr_to - substr_from)]:
                continue
            else:
                new_string += input_string[i]
        return new_string
    else:
        raise ValueError('The specified range is out of the strings bounds.')