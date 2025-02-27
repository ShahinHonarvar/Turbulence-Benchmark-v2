from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:4].lower()
    letters = ''.join(set(substring))
    palindromes = {letters[i] + letters[j] + letters[i] for i in range(len(letters)) for j in range(len(letters) if i != j else 0)}
    return {p for p in palindromes if len(p) >= 3}