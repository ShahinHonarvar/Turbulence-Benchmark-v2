from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[0:9].lower())
    allowed_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = ''.join(sorted(letters.intersection(allowed_letters)))
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            potential_palindrome = ''.join(perm)
            if potential_palindrome == potential_palindrome[::-1]:
                palindromes.add(potential_palindrome)
    return palindromes