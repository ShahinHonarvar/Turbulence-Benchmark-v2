import itertools
import re

def palindromes_between_indices(string):
    english_letters = re.findall('[a-zA-Z]', string)
    palindromes = set()
    for permutation in itertools.permutations(english_letters[4:9]):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes