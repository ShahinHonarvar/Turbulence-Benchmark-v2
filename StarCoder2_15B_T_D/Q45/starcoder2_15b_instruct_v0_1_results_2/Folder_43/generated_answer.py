import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[2:6])
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes