def palindromes_between_indices(string):
    string = ''.join((c for c in string.lower() if c.isalpha()))
    letters = [c for c in string if c.isalpha()]
    arrangements = set([''.join(p) for p in permutations(letters)])
    palindromes = set((p for p in arrangements if len(p) >= 7 and p == p[::-1]))
    return palindromes