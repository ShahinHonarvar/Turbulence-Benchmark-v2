from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 6)
    substring = s[start:end + 1].lower()
    palindromes = set()
    for perm in set(permutations(substring)):
        palindrome_candidate = ''.join(perm)
        if len(palindrome_candidate) >= 4 and palindrome_candidate == palindrome_candidate[::-1]:
            palindromes.add(palindrome_candidate)
    return palindromes