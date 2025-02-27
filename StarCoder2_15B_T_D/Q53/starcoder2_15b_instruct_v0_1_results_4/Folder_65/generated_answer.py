import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(n) + ',}'
    matches = re.findall(pattern, string, flags=re.IGNORECASE)
    palindromes = [word for word in matches if word.lower() == word[::-1]]
    return set(palindromes)