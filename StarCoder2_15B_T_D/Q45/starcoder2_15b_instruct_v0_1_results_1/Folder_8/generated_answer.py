import re
from itertools import permutations

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[1:6])
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5 and palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes