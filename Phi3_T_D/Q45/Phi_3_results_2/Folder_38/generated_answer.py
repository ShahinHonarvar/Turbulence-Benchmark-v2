from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 8)
    substring = s[start:end + 1].lower()
    letters = ''.join(sorted(set(substring), key=substring.index))
    palindromes = set()
    for perm in permutations(letters, 5):
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes