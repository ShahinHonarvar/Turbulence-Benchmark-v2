import re

def palindromes_of_specific_lengths(string):
    """
    Finds all palindromes with lengths between 31 and 51 (both inclusive),
    occurring in the substring from index 18 to index 98 (both inclusive),
    in the given string. Each palindrome must consist of only English letters,
    and the search is case-insensitive.
    """
    pattern = '[a-zA-Z]{' + str(31) + ',' + str(51) + '}'
    sub_string = string[18:99]
    palindromes = re.findall(pattern, sub_string, flags=re.IGNORECASE)
    return set(palindromes)