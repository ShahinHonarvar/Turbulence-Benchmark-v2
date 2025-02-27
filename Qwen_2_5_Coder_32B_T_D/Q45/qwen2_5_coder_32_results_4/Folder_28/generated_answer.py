from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(sorted(filter(lambda x: x.isalpha(), s[1:6]))).lower()
    palindromes = set()
    for perm in permutations(letters):
        p = ''.join(perm)
        if len(p) >= 4 and p == p[::-1]:
            palindromes.add(p)
    return palindromes