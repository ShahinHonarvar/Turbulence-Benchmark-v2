def filter_chars(str):
    """
    Removes all occurrences of characters in a string 
    that fall between 'f' and 'o' in the ASCII table
    (not inclusive) for indices 23 to 83.

    :param str: input string
    :return: string with characters removed as per conditions
    """
    altered_str = ''
    for i in range(len(str)):
        char_code = ord(str[i])
        if 23 <= i < 83 and 'f' < char_code < 'o':
            continue
        altered_str += str[i]
    return altered_str