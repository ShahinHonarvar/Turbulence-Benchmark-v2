import itertools

def palindromes_between_indices(s):
    s = s.lower()
    palindromes = set()
    for permutation in itertools.permutations(s[3:8], 4):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes