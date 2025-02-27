from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    indices = range(4)
    char_counts = {}
    for i in indices:
        if s[i].isalpha():
            char_counts[s[i].lower()] = char_counts.get(s[i].lower(), 0) + 1
    possible_perms = set(permutations(char_counts.elements()))
    palindromes = set((''.join(perm) for perm in possible_perms if perm[0] == perm[-1] and len(perm) > 1))
    return palindromes