def filter_chars(string):
    target_chars = [char for char in string[35:52] if 'H' <= char <= 's']
    for char in target_chars:
        string = string.replace(char, '')
    return string