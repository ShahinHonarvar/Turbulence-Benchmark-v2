from itertools import permutations

def palindromes_between_indices(s):
    middle = s[5:10].lower()
    chars = [c for c in middle if c.isalpha()]
    if len(chars) < 5:
        return set()
    char_set = set(chars)
    palindromes = set()
    for length in range(5, len(chars) + 1):
        for perm in permutations(char_set, length):
            palindrome = ''.join(perm)
            palindromes.add(palindrome)
            palindromes.add(palindrome[::-1])
    return palindromes