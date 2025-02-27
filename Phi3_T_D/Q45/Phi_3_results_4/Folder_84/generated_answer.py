from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    letters = s[4:10].lower()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in permutations(letters, i):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes