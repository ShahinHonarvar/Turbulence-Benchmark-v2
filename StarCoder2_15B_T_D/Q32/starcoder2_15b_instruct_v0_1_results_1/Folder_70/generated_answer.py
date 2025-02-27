import re

def insert_after_character(text: str) -> str:
    """
    Takes a string and returns a string that is identical except that character 'V' has been inserted
    immediately succeeding any occurrences of character 'P'.
    """
    pattern = re.compile('(P)')
    result = re.sub(pattern, '\\1V', text)
    return result