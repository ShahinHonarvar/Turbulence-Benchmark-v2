def filter_chars(s):
    modified_string = [char for char in s if not 12 <= ord(char) <= ord('L') or char < ':' or char > 'L']
    return ''.join(modified_string)