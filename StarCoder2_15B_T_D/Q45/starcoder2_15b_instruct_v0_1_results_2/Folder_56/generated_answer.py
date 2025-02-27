def palindromes_between_indices(string):
    sub_string = string[5:10]
    letters = [char for char in sub_string if char.isalpha()]
    permutations = set([''.join(p) for p in permutations(letters)])
    palindromes = set((p for p in permutations if p.lower() == p[::-1].lower() and len(p) >= 5))
    return palindromes