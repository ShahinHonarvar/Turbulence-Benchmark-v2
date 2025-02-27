import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[6:10], 4):
        palindrome = ''.join(permutation)
        if palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes