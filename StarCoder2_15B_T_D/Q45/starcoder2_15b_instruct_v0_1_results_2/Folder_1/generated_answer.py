import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s.lower() if ch.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[4:8]):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes