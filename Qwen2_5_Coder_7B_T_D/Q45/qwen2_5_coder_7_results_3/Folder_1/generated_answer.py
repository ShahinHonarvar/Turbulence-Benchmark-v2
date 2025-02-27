from itertools import permutations

def palindromes_between_indices(s):
    letters = s[4:8]
    letters = letters.lower()
    unique_letters = set(letters)
    palindromes = set()
    for r in range(5, len(letters) + 1):
        for perm in permutations(unique_letters, r):
            half = ''.join(perm)
            palindrome = half + half[::-1]
            if len(palindrome) <= len(letters):
                palindromes.add(palindrome)
    return palindromes