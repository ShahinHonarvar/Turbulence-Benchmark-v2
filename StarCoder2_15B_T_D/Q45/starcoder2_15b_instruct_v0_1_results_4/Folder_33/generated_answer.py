import re
from itertools import permutations

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[7:10])
    if len(letters) < 4:
        return set()
    combinations = permutations(letters, 4)
    palindromes = set()
    for combination in combinations:
        palindrome = ''.join(combination)
        if palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes