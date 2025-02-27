def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, 8):
        for j in range(i, 8):
            s = letters[i:j]
            if len(s) >= 3 and s.lower() == s[::-1].lower():
                palindromes.add(s)
    return palindromes