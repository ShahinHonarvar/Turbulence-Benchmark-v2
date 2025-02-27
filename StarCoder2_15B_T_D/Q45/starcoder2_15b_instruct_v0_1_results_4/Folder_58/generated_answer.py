import itertools

def palindromes_between_indices(string):
    letters = [ch for ch in string if ch.isalpha()]
    permutations = itertools.permutations(letters, 6)
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes