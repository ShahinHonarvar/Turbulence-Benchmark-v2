from itertools import permutations

def palindromes_between_indices(s):
    middle_part = ''
    if len(s) >= 6:
        middle_part = s[3]
    unique_chars = sorted(set(s[:6].lower()))
    palindromes = set()
    if len(unique_chars) >= 6:
        for perm in permutations(unique_chars, 6):
            halves = perm[:3]
            palindrome_candidate = ''.join(halves) + middle_part + ''.join(reversed(halves))
            palindromes.add(palindrome_candidate)
    return palindromes