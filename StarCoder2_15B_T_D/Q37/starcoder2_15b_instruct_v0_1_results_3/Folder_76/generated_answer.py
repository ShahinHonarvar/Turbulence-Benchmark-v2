def filter_chars(string):
    """
    Given a string, remove all characters that occur between indices 379 and 898,
    both inclusive, and are greater than or equal to 'M' and smaller than or equal to 'v'.
    """

    def condition(char):
        return (ord(char) < 379 or ord(char) > 898) and (char < 'M' or char > 'v')
    return ''.join(filter(condition, string))