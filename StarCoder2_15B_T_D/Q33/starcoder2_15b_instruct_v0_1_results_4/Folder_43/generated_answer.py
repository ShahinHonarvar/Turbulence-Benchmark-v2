import re

def return_vowels(string):
    """
    Returns a list of all vowel English letters between index 22 (inclusive) and index 82 (exclusive)
    that are greater than character N and smaller than or equal to character o. If no such characters
    exist in the specified range, an empty list is returned.

    :param string: The input string.
    :return: A list of vowel English letters that meet the specified criteria.
    """
    vowel_pattern = '[aeiou]'
    vowels = re.findall(vowel_pattern, string)
    filtered_vowels = [vowel for vowel in vowels if vowel > 'N' and vowel <= 'o']
    return filtered_vowels[22:82]