def palindromes_between_indices(s):
    letters = {c.lower() for c in s[2:5]}
    palindromes = {c + d + c for c in letters for d in letters if c != d}
    return palindromes