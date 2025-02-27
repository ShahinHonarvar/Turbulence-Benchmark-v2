import re

def palindromes_between_indices(string):
    letters = re.findall('[a-z]', string.lower())
    palindromes = set()
    for i in range(3, 10):
        for j in range(i + 1, 10):
            for permutation in itertools.permutations(letters[i:j]):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes