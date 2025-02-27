import re

def palindromes_of_specific_lengths(s):
    substring = s[100:201]
    palindromes_set = set()
    for length in range(5, 11):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if re.match('^[a-zA-Z]+$', potential_palindrome):
                if potential_palindrome.lower() == potential_palindrome.lower()[::-1]:
                    palindromes_set.add(potential_palindrome)
    return palindromes_set