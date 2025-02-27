def filter_chars(input_string):
    chars_to_remove = set()
    for i in range(46, 68):
        char = input_string[i]
        if 'H' < char < 's':
            chars_to_remove.add(char)
    result = ''.join([c for c in input_string if c not in chars_to_remove])
    return result