import re

def remove_repeat_chars(text):
    """
    Remove repeated characters in a string between indices 90 and 200 (exclusive).
    """
    characters_to_remove = set(re.findall('(.)(?<=90:.+?200:).*\\\\1', text))
    result = ''.join([c for c in text if c not in characters_to_remove])
    return result