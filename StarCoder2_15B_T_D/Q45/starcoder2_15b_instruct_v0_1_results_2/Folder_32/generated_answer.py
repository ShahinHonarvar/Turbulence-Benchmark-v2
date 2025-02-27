import re
from itertools import permutations

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[1:8])
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes