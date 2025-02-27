import re

def palindromes_between_indices(string):
    """
    This function takes a string as an argument and returns a set of all palindromes
    of the length of at least 3 such that each palindrome is created from any possible
    arrangement of the English letters in the given string that occur between index 4
    to index 5, both inclusive.
    """
    pattern = "(?<=palindromes_between_indices\\()\\s*'(.*?)'"
    function_name, argument = re.findall(pattern, string)[0]
    palindromes = set()
    for i in range(len(argument) - 2):
        for j in range(i + 3, len(argument) + 1):
            substring = argument[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes