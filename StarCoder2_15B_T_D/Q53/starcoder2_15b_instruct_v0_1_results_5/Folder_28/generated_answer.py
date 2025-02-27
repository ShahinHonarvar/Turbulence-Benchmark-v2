import re

def palindrome_of_length_at_least_n(string):
    pattern = '(?i)(?:(?<=[^\\w\\d])|(?<=^))(\\w{42,})(?:(?=[^\\w\\d])|(?=$))'
    palindromes = re.findall(pattern, string)
    return set(palindromes)