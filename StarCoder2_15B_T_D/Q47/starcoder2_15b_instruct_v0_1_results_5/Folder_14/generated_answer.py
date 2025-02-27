import re

def palindromes_of_specific_lengths(string):
    """
    Find palindromes in a given string within a specific index range and with specific lengths.
    """
    start_index = 10
    end_index = 74
    min_length = 6
    max_length = 8
    pattern = '[a-zA-Z]{' + str(min_length) + ',' + str(max_length) + '}'
    palindromes = set()
    sub_string = string[start_index:end_index + 1]
    matches = re.findall(pattern, sub_string, flags=re.IGNORECASE)
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes