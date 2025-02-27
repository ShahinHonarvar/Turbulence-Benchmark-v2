from itertools import permutations

def palindromes_between_indices(s):
    substr = s[4:9].lower()
    unique_chars = sorted(set(substr))
    palindromes = set()
    for char_set in permutations(unique_chars, 4):
        half_palindrome = ''.join(char_set) + ''.join(reversed(char_set))
        if substr.count(half_palindrome[:4]):
            palindromes.add(half_palindrome)
    return set(palindromes)