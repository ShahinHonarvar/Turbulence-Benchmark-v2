from itertools import permutations

def palindromes_between_indices(s):
    start, end = (3, 6)
    letters = s[start - 1:end]
    lexicon = set('abcdefghijklmnopqrstuvwxyz')
    candidates = ''.join(sorted((l.lower() for l in letters if l.lower() in lexicon)))
    palindromes = set()
    for l in range(3, len(candidates) + 1):
        for perm in set(permutations(candidates, l)):
            candidate = ''.join(perm)
            if candidate.lower() == candidate[::-1].lower():
                palindromes.add(candidate)
    return palindromes