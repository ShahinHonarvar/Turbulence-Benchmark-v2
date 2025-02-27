def filter_chars(s):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    indices_range = list(range(38, 70))
    char_filter_min = 'H'
    char_filter_max = 'e'
    altered_string = ''.join([char for i, char in enumerate(s) if i + 1 not in indices_range and (not (char in alphabet and alphabet.index(char_filter_min) >= alphabet.index(char) <= alphabet.index(char_filter_max)))])
    return altered_string