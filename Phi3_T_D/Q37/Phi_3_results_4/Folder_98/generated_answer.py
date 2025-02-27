def filter_chars(input_string):
    target_char = input_string[8:10]
    exclude_range = 'R' <= target_char <= 't'
    result = ''.join([char for char in input_string if char not in target_char or char < 'R' or char > 't'])
    return result