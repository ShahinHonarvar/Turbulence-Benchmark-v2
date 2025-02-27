import re

def palindromes_of_specific_lengths(text: str) -> set:
    """
    Finds all palindromes of specific lengths in a given text.
    """
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(136) + ',' + str(151) + '}'
    subtext = text[106:281]
    matches = re.findall(pattern, subtext, flags=re.I)
    for match in matches:
        if match.lower() == match[::-1].lower():
            palindromes.add(match)
    return palindromes