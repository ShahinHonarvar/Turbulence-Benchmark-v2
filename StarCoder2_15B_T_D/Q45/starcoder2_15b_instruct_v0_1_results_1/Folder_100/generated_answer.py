import re

def palindromes_between_indices(string):
    pattern = re.compile('[a-zA-Z]+')
    letters = pattern.findall(string)
    letters = letters[0:6]
    permutations = set(itertools.permutations(letters))
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes