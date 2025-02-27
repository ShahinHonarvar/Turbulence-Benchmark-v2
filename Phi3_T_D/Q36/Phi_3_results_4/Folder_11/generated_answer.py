def filter_chars(input_string):
    new_string = input_string[:86] + ''.join([char for char in input_string[86:93] if not 'E' < char < '~']) + input_string[93:]
    return new_string