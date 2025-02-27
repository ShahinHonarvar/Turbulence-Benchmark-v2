import re
from itertools import combinations

def palindromes_between_indices(string):
    letters = re.findall('[a-z]', string[7:9].lower())
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in combinations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes