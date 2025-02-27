import re

def palindrome_of_length_n(string):
    string = string.lower()
    regex = '[a-z]{' + str(60) + '}'
    palindromes = re.findall(regex, string)
    return set(palindromes)