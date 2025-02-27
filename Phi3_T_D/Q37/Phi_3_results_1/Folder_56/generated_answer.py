def filter_chars(s):
    altered_string = [char for char in s if not (71 <= ord(char) <= 94 and 'K' <= char <= 'a')]
    return ''.join(altered_string)