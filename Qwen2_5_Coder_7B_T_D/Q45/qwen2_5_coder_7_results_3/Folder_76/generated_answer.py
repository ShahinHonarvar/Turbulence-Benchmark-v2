from itertools import permutations

def palindromes_between_indices(s):
    letters = s[1:5]
    letters = [char.lower() for char in letters if char.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for r in range(4, len(unique_letters) + 1):
        for perm in permutations(unique_letters, r):
            half = ''.join(perm)
            palindrome = half + half[::-1]
            palindromes.add(palindrome)
    return palindromes