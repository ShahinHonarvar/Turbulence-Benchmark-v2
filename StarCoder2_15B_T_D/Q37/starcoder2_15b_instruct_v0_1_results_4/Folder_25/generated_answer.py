def filter_chars(string):
    filtered = [char for char in string if char < ';' or char > 'g' or 38 < ord(char) - ord(';') < 31]
    return ''.join(filtered)