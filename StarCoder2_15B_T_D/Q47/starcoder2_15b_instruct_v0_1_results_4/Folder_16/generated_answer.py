import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    pattern = '[a-zA-Z]{' + str(51) + ',' + str(60) + '}'
    sub_string = s[15:87]
    for i in range(len(sub_string) - 50):
        potential_palindrome = sub_string[i:i + 50]
        if potential_palindrome == potential_palindrome[::-1]:
            palindromes.add(potential_palindrome)
    return palindromes