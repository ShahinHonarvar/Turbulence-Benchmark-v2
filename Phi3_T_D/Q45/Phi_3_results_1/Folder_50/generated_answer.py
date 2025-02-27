from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    letters_sub = s[4:9].lower()
    palindromes = set()
    for i in range(len(letters_sub) - 4):
        for j in range(i + 4, len(letters_sub) + 1):
            substring = letters_sub[i:j]
            perms = set([''.join(p) for p in permutations(substring)])
            palindromes.update(filter(is_palindrome, perms))
    return palindromes