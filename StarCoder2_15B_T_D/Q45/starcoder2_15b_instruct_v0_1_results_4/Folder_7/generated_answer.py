import itertools
import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string)
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes