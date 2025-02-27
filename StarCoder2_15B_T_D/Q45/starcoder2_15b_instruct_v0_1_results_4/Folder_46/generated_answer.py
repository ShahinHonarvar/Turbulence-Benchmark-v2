import re

def palindromes_between_indices(string):
    letters = re.findall('[a-z]', string.lower())
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 1, 10):
            for permutation in permutations(letters[i:j]):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes

def permutations(letters):
    if len(letters) <= 1:
        yield letters
    else:
        for permutation in permutations(letters[1:]):
            for i in range(len(letters)):
                yield (permutation[:i] + letters[0:1] + permutation[i:])