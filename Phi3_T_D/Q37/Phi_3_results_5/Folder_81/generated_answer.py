def filter_chars(s):
    lower_boundry = ord('8')
    upper_boundry = ord('m')
    return ''.join((char for i, char in enumerate(s) if not (19 <= i <= 92 and lower_boundry <= ord(char) <= upper_boundry)))