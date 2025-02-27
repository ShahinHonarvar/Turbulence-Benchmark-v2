def filter_chars(string):
    filtered = [char for char in string if char < 'H' or char > 's' or 35 > string.index(char) or (string.index(char) > 51)]
    return ''.join(filtered)