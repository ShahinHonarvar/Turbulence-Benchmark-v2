def filter_chars(string):
    filtered_chars = [char for char in string if char < '*' or char > 'b' or (char < '42' or char > '97')]
    return ''.join(filtered_chars)