from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:6].lower()
    letters = ''.join(filter(str.isalpha, substring))
    if len(letters) < 2:
        return set()
    palindromes = set()
    for size in range(4, len(letters) + 1, 2):
        for perm in set(permutations(letters, size)):
            palindrome_candidate = ''.join(perm)
            if palindrome_candidate == palindrome_candidate[::-1]:
                palindromes.add(palindrome_candidate)
    return palindromes