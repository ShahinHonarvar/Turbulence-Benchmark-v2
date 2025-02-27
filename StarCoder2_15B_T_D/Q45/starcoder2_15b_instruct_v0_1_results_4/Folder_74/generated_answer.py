def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha()]
    arrangements = set(itertools.permutations(letters))
    palindromes = {''.join(a) for a in arrangements if a == a[::-1]}
    return palindromes