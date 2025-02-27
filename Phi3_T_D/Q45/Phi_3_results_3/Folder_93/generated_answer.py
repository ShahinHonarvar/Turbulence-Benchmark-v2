from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    unique_letters = set(s)
    palindromes = set()
    if len(unique_letters) < 6:
        return palindromes
    for perm in permutations(unique_letters, 6):
        palindrome = ''.join(perm) + ''.join(reversed(perm))
        palindromes.add(palindrome)
        for i in range(4):
            new_palindrome = palindrome[:i] + palindrome[i].upper() + palindrome[i + 1:-i - 1] + palindrome[-i].upper() + palindrome[-i - 1]
            palindromes.add(new_palindrome)
    return palindromes