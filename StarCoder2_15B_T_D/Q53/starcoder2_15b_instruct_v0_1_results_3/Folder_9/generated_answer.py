import re

def palindrome_of_length_at_least_n(input_string):
    pattern = '\\b[a-zA-Z]{95,}\\b'
    matches = re.findall(pattern, input_string, flags=re.IGNORECASE)
    palindromes = [word for word in matches if word == word[::-1]]
    return set(palindromes)