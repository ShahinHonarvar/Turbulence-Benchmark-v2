from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:10]
    letters = ''.join(sorted(set(substring.lower())))
    center = letters[len(letters) // 2]
    half_palindromes = {center + ''.join(p) + center[::-1] for p in permutations(letters, (len(letters) - 1) // 2)}
    palindromes = set()
    for p in half_palindromes:
        if len(p) >= 5:
            palindromes.add(p)
    return palindromes