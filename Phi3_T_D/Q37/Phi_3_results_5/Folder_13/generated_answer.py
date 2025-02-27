def filter_chars(input_string):
    alpha_numeric = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for index in range(124, 855):
        char_to_remove = input_string[index]
        if alpha_numeric.find(char_to_remove) >= alpha_numeric.find('9') and alpha_numeric.find(char_to_remove) <= alpha_numeric.find('s'):
            input_string = input_string.replace(char_to_remove, '')
    return input_string