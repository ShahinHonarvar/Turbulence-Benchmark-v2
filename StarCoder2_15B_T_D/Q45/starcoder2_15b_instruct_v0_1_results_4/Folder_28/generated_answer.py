def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = {''.join(letters[i:j]) for i in range(1, 6) for j in range(i, 6)}
    return {p for p in palindromes if len(p) >= 4 and p == p[::-1]}