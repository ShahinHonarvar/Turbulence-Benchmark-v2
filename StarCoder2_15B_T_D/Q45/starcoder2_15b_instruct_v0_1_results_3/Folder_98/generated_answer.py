import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[3:6]):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes