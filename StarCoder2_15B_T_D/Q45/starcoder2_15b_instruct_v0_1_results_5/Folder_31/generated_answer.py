import re
from itertools import permutations

def palindromes_between_indices(s):
    pattern = re.compile('[a-zA-Z]')
    letters = pattern.findall(s)
    palindromes = set()
    for permutation in permutations(letters[1:9], 6):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes