from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    relevant_chars = s[2:10]
    palindromes = set()
    used_perms = set()
    for l in range(4, len(relevant_chars) + 1):
        for perm in set(permutations(relevant_chars, l)):
            perm_str = ''.join(perm).lower()
            if perm_str not in used_perms:
                used_perms.add(perm_str)
                if is_palindrome(perm_str):
                    palindromes.add(perm_str)
    return palindromes