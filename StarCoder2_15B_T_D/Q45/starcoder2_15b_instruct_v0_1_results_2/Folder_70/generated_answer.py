def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(1, len(letters) - 6):
        for j in range(i + 4, len(letters) + 1):
            palindromes.add(''.join(letters[i:j]).lower())
    return palindromes