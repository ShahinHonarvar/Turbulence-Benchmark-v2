def palindromes_between_indices(string):
    letters = [c for c in string[4:9] if c.isalpha()]
    arrangements = [''.join(p) for p in itertools.permutations(letters)]
    palindromes = [p for p in arrangements if len(p) >= 5 and p == p[::-1]]
    return set(palindromes)