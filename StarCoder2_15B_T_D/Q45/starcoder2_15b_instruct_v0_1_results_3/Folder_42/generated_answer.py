def palindromes_between_indices(s):
    letters = [c for c in s.lower() if c.isalpha()]
    palindromes = set()
    for i in range(6, 9):
        for j in range(i + 1, 9):
            for k in range(j + 1, 9):
                palindromes.add(letters[i] + letters[j] + letters[k] + letters[k] + letters[j] + letters[i])
    return palindromes