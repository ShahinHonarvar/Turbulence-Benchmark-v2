from itertools import permutations

def palindromes_between_indices(s):
    length = len(s[5:8])
    if length < 4:
        return set()
    middle_part = s[5:8].lower()
    possible_permutations = set(permutations(middle_part))
    palindromes = set()
    for perm in possible_permutations:
        half = ''.join(perm[:length // 2])
        full_palindrome = half + (half[::-1] if length % 2 == 0 else half[::-1][1:])
        palindromes.add(full_palindrome)
    return palindromes