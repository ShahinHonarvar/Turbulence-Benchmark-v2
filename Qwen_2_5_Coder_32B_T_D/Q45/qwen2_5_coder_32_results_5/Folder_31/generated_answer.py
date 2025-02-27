from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    letters = ''.join(filter(lambda x: x.lower() in ascii_lowercase, s[1:9])).lower()
    palindromes = set()
    for perm in permutations(letters, len(letters)):
        p = ''.join(perm)
        if len(p) >= 6 and p == p[::-1]:
            palindromes.add(p)
    return palindromes