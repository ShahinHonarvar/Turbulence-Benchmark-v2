import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(86) + ',}'
    palindromes = set(re.findall(pattern, string))
    filtered_palindromes = set()
    for palindrome in palindromes:
        if palindrome.lower() == palindrome.lower()[::-1]:
            filtered_palindromes.add(palindrome)
    return filtered_palindromes