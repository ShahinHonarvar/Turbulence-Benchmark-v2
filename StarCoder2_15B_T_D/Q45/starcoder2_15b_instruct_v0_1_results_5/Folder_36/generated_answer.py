import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[5:9]):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes