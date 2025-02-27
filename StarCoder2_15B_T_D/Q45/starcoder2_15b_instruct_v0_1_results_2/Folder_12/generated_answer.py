import itertools

def palindromes_between_indices(s):
    palindromes = set()
    letters = [c for c in s[3:9].lower() if c.isalpha()]
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes