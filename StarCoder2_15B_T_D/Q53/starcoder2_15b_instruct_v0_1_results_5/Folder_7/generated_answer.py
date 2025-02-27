import re

def palindrome_of_length_at_least_n(string):
    return {palindrome for palindrome in set(re.findall('(?i)(\\w{122,})', string)) if palindrome.isalpha()}