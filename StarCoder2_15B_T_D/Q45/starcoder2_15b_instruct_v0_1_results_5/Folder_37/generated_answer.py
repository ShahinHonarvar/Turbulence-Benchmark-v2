import itertools

def palindromes_between_indices(string):
    letters = set(string.lower())
    palindromes = set()
    for permutation in itertools.permutations(letters, 5):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes