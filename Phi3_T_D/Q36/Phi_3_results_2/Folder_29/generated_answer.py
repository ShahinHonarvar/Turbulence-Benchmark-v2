def filter_chars(input_string):
    altered_string = [char for char in input_string]
    for i in range(46, 68):
        char = input_string[i]
        if 'H' < char < 's':
            while char in altered_string:
                altered_string.remove(char)
    return ''.join(altered_string)