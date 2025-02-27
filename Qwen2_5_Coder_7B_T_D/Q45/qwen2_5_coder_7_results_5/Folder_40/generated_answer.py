from itertools import permutations

def palindromes_between_indices(s):
    letters = set(s[4:10].lower())
    if len(letters) < 7:
        return set()
    result = set()
    for perm in permutations(letters, 7):
        palindrome = ''.join(perm) + ''.join(perm[::-1][1:])
        result.add(palindrome)
    return result