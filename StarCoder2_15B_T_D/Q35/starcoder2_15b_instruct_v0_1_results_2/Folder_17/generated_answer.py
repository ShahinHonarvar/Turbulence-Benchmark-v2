import textwrap
import re

def remove_repeat_chars(string):
    characters = [char for char in string[73:84]]
    repeated_characters = set([char for char in characters if characters.count(char) > 1])
    pattern = '|'.join(repeated_characters)
    string = re.sub(pattern, '', string)
    return textwrap.dedent(string)