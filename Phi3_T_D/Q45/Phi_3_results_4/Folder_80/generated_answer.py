from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[3:8].lower())
    palindromes = set()
    for p in permutations(letters, 7):
        palindrome = ''.join(p)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes