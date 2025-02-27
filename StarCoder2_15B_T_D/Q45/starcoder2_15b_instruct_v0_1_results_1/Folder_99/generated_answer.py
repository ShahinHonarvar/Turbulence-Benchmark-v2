import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[4:9]):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 3 and palindrome.lower() == palindrome[::-1].lower():
            palindromes.add(palindrome)
    return palindromes