def palindromes_between_indices(s):
    letters = [c for c in s.lower() if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 3):
        for j in range(i + 3, min(i + 6, len(letters))):
            palindromes.add(letters[i:j + 1][::-1])
    return palindromes