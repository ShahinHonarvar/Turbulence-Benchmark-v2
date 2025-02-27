def filter_chars(input_string):
    begin, end = (27, 29)
    forbidden_chars = [chr(i) for i in range(ord(';'), ord('b') + 1)]
    altered_string = ''.join((char for char in input_string if char not in forbidden_chars or not begin <= input_string.index(char) <= end))
    return altered_string