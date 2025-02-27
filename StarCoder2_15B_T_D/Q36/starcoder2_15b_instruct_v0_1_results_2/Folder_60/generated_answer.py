def filter_chars(string):
    filtered = [char for char in string if not (char > 'f' and char < 'o')]
    return ''.join(filtered)