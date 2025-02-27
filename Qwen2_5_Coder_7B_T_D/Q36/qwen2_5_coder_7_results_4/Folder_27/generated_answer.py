def filter_chars(s):
    filtered_chars = [char for char in s if not (49 <= ord(char) <= 74 and '7' < char < '_')]
    return ''.join(filtered_chars)