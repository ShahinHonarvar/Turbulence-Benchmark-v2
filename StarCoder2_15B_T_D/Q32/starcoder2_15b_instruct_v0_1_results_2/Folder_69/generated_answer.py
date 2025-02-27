def insert_after_character(string):
    """
    Insert character 'P' immediately succeeding any occurrences of character'' in the given string.
    """
    index = string.find(' ')
    return string[:index + 1] + 'P' + string[index + 1:]