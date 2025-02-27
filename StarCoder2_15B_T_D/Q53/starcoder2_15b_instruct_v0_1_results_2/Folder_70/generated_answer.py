import re

def palindrome_of_length_at_least_n(string):
    pattern = '[a-zA-Z]{' + str(11) + ',}'
    palindromes = re.findall(pattern, string)
    filtered_palindromes = [palindrome for palindrome in palindromes if palindrome == palindrome[::-1]]
    return set(filtered_palindromes)