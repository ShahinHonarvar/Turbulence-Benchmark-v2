def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(len(letters) - 6):
        for j in range(i + 6, len(letters)):
            palindromes.add(''.join(letters[i:j + 1]).lower())
    return {p for p in palindromes if len(p) >= 7 and p == p[::-1]}